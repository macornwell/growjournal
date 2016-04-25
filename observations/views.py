from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render
from core.views import get_add_model_form
from observations.models import TemperatureReading, WeatherReading, Observation
from observations.forms import TemperatureReadingForm, WeatherReadingForm, ObservationForm

ADD_OBSERVATION_TEMPLATE = 'observations/add_observation_model.html'


def add_temperature_reading(request):
    return get_add_model_form(request, ADD_OBSERVATION_TEMPLATE, TemperatureReading, 'Temperature Reading', 'datetime', TemperatureReadingForm)


def add_weather_reading(request):
    return get_add_model_form(request, ADD_OBSERVATION_TEMPLATE, WeatherReading, 'Weather Reading', 'datetime', WeatherReadingForm)


def add_observation(request):
    return get_add_model_form(request, ADD_OBSERVATION_TEMPLATE, Observation, 'Observation', 'observation_date', ObservationForm)


def add_temperature_reading_alpha(request):
    return render(request, 'observations/add_model_wizard.html')
