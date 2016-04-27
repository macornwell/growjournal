from django.shortcuts import render
from django.contrib import messages
from core.models import Note
from core.forms import NoteForm


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


def add_note(request):
    user = request.user
    notesForUser = Note.objects.filter(user_id=user.id)
    generator = lambda: (('notes', notesForUser),)
    return get_add_model_form(request, 'core/add_note.html', Note, 'Note', 'datetime', NoteForm, additionalDataGenerator=generator)
