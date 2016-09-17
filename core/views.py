from django.shortcuts import render
from django.contrib import messages
from core.models import WebsiteFeedback
from core.forms import FeedbackForm


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
