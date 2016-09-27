from django.views.generic.list import ListView
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.urlresolvers import reverse
from core.models import Site, Unit, Project
from core.forms import SiteForm, UnitForm, ProjectForm
from core.services import get_user_core_settings

WIZARD_FORM_TEMPLATE = 'wizard/wizard-form.html'

def get_back_url(url):
    return "window.location.href = '{0}'".format(url)

def get_back_to_settings_string():
    url = reverse('setup')
    return get_back_url(url)


class ListEntry:
    edit_url = None
    model = None

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)


def list_model_view(request, title, addUrl, singularName, pluralName, listEntries, template=None, modelTemplatePath=None, backButtonUrl=None):
    data = {
        'title': title,
        'add_url': addUrl,
        'singular_name': singularName,
        'plural_name': pluralName,
        'list_entries': listEntries,
        'model_template_path': modelTemplatePath,
        'back_button_url': backButtonUrl,
    }
    if not template:
        return render(request, 'model-list.html', data)
    else:
        return render(request, template, data)


class CRUDView:
    model_type = None
    form_type = None
    list_view_name = None
    singular = None
    plural = None
    back_list_url = None

    def get_edit_url(self):
        return 'edit_{0}'.format(self.singular.lower())

    def get_list_url(self):
        return self.plural.lower()

    def get_add_url(self):
        return 'add_{0}'.format(self.singular.lower())

    def get_id(self, model):
        raise NotImplemented('get_id')

    def get_model(self, modelID):
        raise NotImplemented('get_model')

    def post(self, request, model=None):
        raise NotImplemented('post')

    def create_form(self, request):
        return self.form_type()

    def list(self, request):
        entries = []
        for model in self.model_type.objects.all():
            entries.append(ListEntry(model=model, edit_url=reverse(self.get_edit_url(), kwargs={'modelID': self.get_id(model)})))
        backUrl = self.back_list_url
        if not backUrl:
            backUrl = reverse('settings')
        backUrl = get_back_url(backUrl)
        return list_model_view(request, self.plural, reverse(self.get_add_url()), self.singular, self.plural, entries, backButtonUrl=backUrl)

    def add(self, request):
        data = {}
        if request.POST:
            return self.post(request)
        form = self.create_form(request)
        data['form'] = form
        return render(request, WIZARD_FORM_TEMPLATE, data)

    def edit(self, request, modelID):
        data = {}
        model = self.get_model(modelID)
        if request.POST:
            if 'delete-button' in request.POST:
                return self.delete(request, model)
            return self.post(request, model)
        form = self.create_form(request)
        form.apply_instance(model)
        data['form'] = form
        data['is_editing_model'] = True
        return render(request, WIZARD_FORM_TEMPLATE, data)

    def delete(self, request, model):
        model.delete()
        return self.list(request)

"""
Sites
"""

def change_site(request, siteID):
    user = request.user
    if user.is_authenticated():
        site = Site.objects.get(site_id=siteID)
        if site:
            settings = get_user_core_settings(user)
            settings.active_site = site
            settings.save()
    return redirect('home')


class SiteCRUDView(CRUDView):
    model_type = Site
    form_type = SiteForm
    singular = 'Site'
    plural = 'Sites'

    def get_id(self, model):
        return model.site_id

    def get_model(self, modelID):
        return Site.objects.get(site_id=modelID)

    def post(self, request, site=None):
        data = request.POST
        name = data['name']
        isJoinable = 'public-joinable' in data
        isViewable = 'public-viewable' in data
        if not site:
            site = Site()
        site.user = request.user
        site.is_public_joinable = isJoinable
        site.is_public_viewable = isViewable
        site.name = name
        site.save()
        return self.list(request)

    def list(self, request):
        entries = []
        for site in Site.objects.filter(user=request.user):
            entries.append(ListEntry(model=site, edit_url=reverse(self.get_edit_url(), kwargs={'modelID': self.get_id(site)})))
        return list_model_view(request, self.plural, reverse(self.get_add_url()), self.singular, self.plural, entries, backButtonUrl=get_back_to_settings_string())


class UnitCRUDView(CRUDView):
    model_type = Unit
    form_type = UnitForm
    singular = 'Unit'
    plural = 'Units'

    def get_model(self, modelID):
        return Unit.objects.get(unit_id=modelID)

    def get_id(self, model):
        return model.unit_id

    def post(self, request, model=None):
        name = request.POST['name']
        if not model:
            model = Unit()
        model.name = name
        model.save()
        return self.list(request)


class ProjectCRUDView(CRUDView):
    model_type = Project
    form_type = ProjectForm
    singular = 'Project'
    plural = 'Projects'

    def get_model(self, modelID):
        return Project.objects.get(project_id=modelID)

    def get_id(self, model):
        return model.project_id

    def post(self, request, model=None):
        name = request.POST['name']
        siteID = request.POST['site']
        isPerpetual = 'is-perpetual' in request.POST
        description = request.POST['description']
        isPublic = 'is-public-viewable' in request.POST
        if not model:
            model = Project()
        model.name = name
        model.site = Site.objects.get(site_id=siteID)
        model.is_perpetual = isPerpetual
        model.description = description
        model.is_public_viewable = isPublic
        model.save()
        return self.list(request)