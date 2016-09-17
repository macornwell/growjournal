from django.contrib import admin
from weather.models import TemperatureReading, WeatherReading

# Register your models here.
admin.site.register(TemperatureReading)
admin.site.register(WeatherReading)