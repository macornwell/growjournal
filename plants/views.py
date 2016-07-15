from django.shortcuts import render
from plants.models import Harvest, Watering, Bloom, PlantProductivityReport, Resource, PlantReport
from plants.forms import PlantProductivityForm, BloomForm, HarvestForm, WateringForm, ResourceForm, cultivar_species_validator, PlantReportForm
from core.views import get_add_model_form

ADD_PLANTS_TEMPLATE = 'plants/add_plant_model.html'

def add_resource(request):
    return get_add_model_form(request, ADD_PLANTS_TEMPLATE, Resource, 'Resource', None, ResourceForm, customValidator=cultivar_species_validator)


def add_harvest(request):
    return get_add_model_form(request, ADD_PLANTS_TEMPLATE, Harvest, 'Harvest', 'datetime', HarvestForm)


def add_watering(request):
    return get_add_model_form(request, ADD_PLANTS_TEMPLATE, Watering, 'Watering', 'datetime', WateringForm)


def add_plant_productivity(request):
    return get_add_model_form(request, ADD_PLANTS_TEMPLATE, PlantProductivityReport, 'Plant Productivity', 'datetime', PlantProductivityForm, customValidator=cultivar_species_validator)


def add_plant_report(request):
    return get_add_model_form(request, ADD_PLANTS_TEMPLATE, PlantReport, 'Plant Report', 'datetime', PlantReportForm, customValidator=cultivar_species_validator)


def add_bloom(request):
    return get_add_model_form(request, ADD_PLANTS_TEMPLATE, Bloom, 'Bloom', 'start', BloomForm, customValidator=cultivar_species_validator)
