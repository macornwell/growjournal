from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy, reverse
from core.models import Site, Unit, Project
from core.forms import SiteForm, UnitForm, ProjectForm
from core.services import get_user_core_settings
from django_wizard_crud_view.views import CRUDView, ListEntry

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
        return self.list_model_view(request, self.plural, reverse(self.get_add_url()), self.singular, self.plural, entries, backButtonUrl=reverse('setup'))


class UnitCRUDView(CRUDView):
    model_type = Unit
    form_type = UnitForm
    singular = 'Unit'
    plural = 'Units'

    def get_back_list_url(self):
        return reverse('setup')

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

    def get_back_list_url(self):
        return reverse('setup')

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