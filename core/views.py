from django.shortcuts import render, redirect
from django.contrib import messages
from core.models import WebsiteFeedback, Site
from core.forms import FeedbackForm, SiteForm

WIZARD_FORM_TEMPLATE = 'wizard-form.html'


def add_site(request):
    data = {}
    if request.POST:
        return post_site(request)
    form = SiteForm()
    data['form'] = form
    return render(request, WIZARD_FORM_TEMPLATE, data)


def post_site(request):
    data = request.POST
    name = data['name']
    isJoinable = 'public-joinable' in data
    isViewable = 'public-viewable' in data
    site = Site()
    site.user = request.user
    site.is_public_joinable = isJoinable
    site.is_public_viewable = isViewable
    site.name = name
    site.save()
    return redirect('setup')


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


def add_feedback(request):
    user = request.user
    #Replace with QueryLayer.get_feedback_by_user_id
    feedbackForByUser = WebsiteFeedback.objects.filter(user_id=user.id)
    generator = lambda: (('feedback', feedbackForByUser),)
    return get_add_model_form(request, 'core/add_feedback.html', WebsiteFeedback, 'WebsiteFeedback', 'datetime', FeedbackForm, additionalDataGenerator=generator)
