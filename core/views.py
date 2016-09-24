from django.views.generic.list import ListView
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.urlresolvers import reverse
from core.models import WebsiteFeedback, Site
from core.forms import FeedbackForm, SiteForm
from core.services import get_user_core_settings

WIZARD_FORM_TEMPLATE = 'wizard/wizard-form.html'

def get_back_to_settings_string():
    url = reverse('setup')
    return "window.location.href = '{0}'".format(url)


def get_add_model_form(request, templatePath, modelType, modelTypeFriendlyName, datePropertyName, formType, customValidator=None, additionalDataGenerator=None):
    lastReading = ''
    if datePropertyName:
        lastReadingObj = modelType.objects.order_by('-{0}'.format(datePropertyName)).first()
        if lastReadingObj:
            lastReading = str(lastReadingObj)
    if request.method == 'POST':
        form = formType(request.POST)
        if form.is_valid():
            passedCustomValidation = True
            if customValidator:
                passedCustomValidation = customValidator(request, form)
                if not passedCustomValidation:
                    messages.error(request, '{0} failed validation.'.format(modelType.__name__))
            if passedCustomValidation:
                model = form.save(commit=False)
                model.user = request.user
                model.save()
                messages.info(request, '{0} Saved!'.format(modelType.__name__))
                lastReading = str(model)
        else:
            messages.error(request, 'Unable to save {0}.'.format(modelType.__name__))
    else:
        form = formType()
    data = {
        'form': form,
        'last_object': lastReading,
        'add_model_type': modelTypeFriendlyName,
    }
    if additionalDataGenerator:
        for key, value in additionalDataGenerator():
            data[key] = value
    return render(request, templatePath, data)


class ListEntry:
    edit_url = None
    model = None

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)



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


def add_site(request):
    data = {}
    if request.POST:
        return post_site(request)
    form = SiteForm()
    data['form'] = form
    return render(request, WIZARD_FORM_TEMPLATE, data)


def post_site(request, site=None):
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
    return redirect('setup')


def edit_site(request, siteID):
    data = {}
    site = Site.objects.get(site_id=siteID)
    if request.POST:
        if 'delete-button' in request.POST:
            return delete_site(request, site)
        return post_site(request, site)
    form = SiteForm()
    form.apply_instance(site)
    data['form'] = form
    data['is_editing_model'] = True
    return render(request, WIZARD_FORM_TEMPLATE, data)


def delete_site(request, site):
    site.delete()
    return redirect('sites')


def list_sites(request):
    entries = []
    for site in Site.objects.filter(user=request.user):
        entries.append(ListEntry(model=site, edit_url=reverse('edit_site', kwargs={'siteID': site.site_id})))
    return list_model_view(request, 'Sites', reverse('add_site'), 'Site', 'Sites', entries, backButtonUrl=get_back_to_settings_string())


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







def add_feedback(request):
    user = request.user
    #Replace with QueryLayer.get_feedback_by_user_id
    feedbackForByUser = WebsiteFeedback.objects.filter(user_id=user.id)
    generator = lambda: (('feedback', feedbackForByUser),)
    return get_add_model_form(request, 'core/add_feedback.html', WebsiteFeedback, 'WebsiteFeedback', 'datetime', FeedbackForm, additionalDataGenerator=generator)
