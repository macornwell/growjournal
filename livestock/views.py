from django.shortcuts import render
from core.views import get_add_model_form
from livestock.models import EggCollection, AnimalReport
from livestock.forms import EggCollectionForm, AnimalReportForm

ADD_LIVESTOCK_TEMPLATE = 'livestock/add_livestock_model.html'


def add_egg_collection(request):
    return get_add_model_form(request, ADD_LIVESTOCK_TEMPLATE, EggCollection, 'Eggs', 'datetime', EggCollectionForm)


def add_animal_report(request):
    return get_add_model_form(request, ADD_LIVESTOCK_TEMPLATE, AnimalReport, 'Animal Report', 'datetime', AnimalReportForm)