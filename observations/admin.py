from django.contrib import admin
from observations.models import TemperatureReading, WeatherReading, Observation

# Register your models here.

admin.site.register(TemperatureReading)
admin.site.register(WeatherReading)
admin.site.register(Observation)
