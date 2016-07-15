from django.shortcuts import render
from core.views import get_add_model_form
from work.models import WorkCompleted
from work.forms import WorkCompletedForm

def add_work_completed(request):
    return get_add_model_form(request, 'work/add_work_model.html', WorkCompleted, 'Work Completed', 'datetime', WorkCompletedForm )
"""

def add_work_completed(request):
    lastReadingObj = WorkCompleted.objects.order_by('-{0}'.format('datetime')).first()
    lastReading = ''
    if lastReadingObj:
        lastReading = str(lastReadingObj)
    data = {
        'last_object': lastReading,
        'add_model_type': 'WorkCompleted',
        'formData': {
            'project': {
                'type': 'dropdown',
                },
            'datetime': {
                'type': 'text',
            },
            'summary': {
                'type': 'text',
            },
            'work': {
                'type': 'textarea',
            },
        },
    }

    return render(request, context=data, template_name='core/wizard_add.html')
"""
