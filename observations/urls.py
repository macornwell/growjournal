from django.conf.urls import url
from observations.views import add_temperature_reading

urlpatterns = [
    url('^add/observations/temperature', name='add_temperature', view=add_temperature_reading)
]