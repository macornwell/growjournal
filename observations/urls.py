from django.conf.urls import url
from observations.views import add_temperature_reading, add_weather_reading, add_observation, add_temperature_reading_alpha

urlpatterns = [
    url('^add/observations/observation', name='add_observation', view=add_observation),
    url('^add/observations/temperature', name='add_temperature', view=add_temperature_reading),
    url('^add/observations/alpha-temperature', name='add_temperature_alpha', view=add_temperature_reading_alpha),
    url('^add/observations/weather', name='add_weather', view=add_weather_reading)
]