from django.shortcuts import render
from django.contrib import messages


def get_add_model_form(request, templatePath, modelType, modelTypeFriendlyName, datePropertyName, formType):
    lastReading = ''
    lastReadingObj = modelType.objects.order_by('-{0}'.format(datePropertyName)).first()
    if lastReadingObj:
        lastReading = str(lastReadingObj)
    if request.method == 'POST':
        form = formType(request.POST)
        if form.is_valid():
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
    return render(request, templatePath, data)