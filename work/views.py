from django.shortcuts import render
from core.views import get_add_model_form
from work.models import WorkCompleted
from work.forms import WorkCompletedForm

def add_work_completed(request):
    return get_add_model_form(request, 'work/add_work_model.html', WorkCompleted, 'Work Completed', 'datetime', WorkCompletedForm )
