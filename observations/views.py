from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render
from core.views import get_add_model_form
from observations.models import Observation, ObservationType
from taxonomy.models import ANIMAL_KINGDOM_NAME, PLANT_KINGDOM_NAME, Kingdom
from observations.forms import ObservationForm

ADD_OBSERVATION_TEMPLATE = 'observations/add_observation_model.html'

def _get_kingdoms_in_order():
    return sorted(Kingdom.objects.all(), key=lambda x: x.name)

def add_observation(request):
    observationTypes = [t for t in ObservationType.objects.all()]
    animalTypes = [t for t in observationTypes if t.kingdom_specific and t.kingdom_specific.name is ANIMAL_KINGDOM_NAME]
    plantTypes = [t for t in observationTypes if t.kingdom_specific and t.kingdom_specific.name is PLANT_KINGDOM_NAME]
    otherTypes = [t for t in observationTypes if not t.kingdom_specific]
    data = {
        'kingdomDict': _get_kingdoms_in_order(),
        'plant_types': plantTypes,
        'animal_types': animalTypes,
        'other_types': otherTypes,
    }
    return render(request, 'observations/add_observation.html', context=data)

