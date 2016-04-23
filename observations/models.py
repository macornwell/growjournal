from datetime import datetime
from django.utils import timezone
import django.templatetags.tz as DjangoTZ
from django.db import models
from core.models import BaseUserActivityModel, Project
import pytz

LOCAL = pytz.timezone('US/Central')


TEMPERATURE_UNITS = (
    ('f', 'Fahrenheit'),
    ('c', 'Celsius')
)

WEATHER_STATES = (
    ('s', 'Sunny'),
    ('p', 'Partly Cloudy'),
    ('c', 'Cloudy'),
    ('o', 'Overcast'),
    ('r', 'Rainy'),
    ('f', 'Freeze'),
    ('r', 'Frost'),
)


class Observation(BaseUserActivityModel):
    observation_id = models.AutoField(primary_key=True)
    project = models.ForeignKey(Project, blank=True, null=True)
    observation_date = models.DateTimeField()
    summary = models.CharField(max_length=50, blank=True, null=True)
    observation = models.TextField()


class TemperatureReading(BaseUserActivityModel):
    temperature_reading_id = models.AutoField(primary_key=True)
    value = models.DecimalField(decimal_places=2, max_digits=8)
    datetime = models.DateTimeField(default=timezone.now)
    unit = models.CharField(max_length=1, choices=TEMPERATURE_UNITS, default=TEMPERATURE_UNITS[0][0])

    def __str__(self):
        return '{0}: {1}{2}\u00B0'.format(self.datetime.astimezone(LOCAL).strftime('%b %d %Y at %H:%M:%S'), self.value, self.unit)


class WeatherReading(BaseUserActivityModel):
    weather_reading_id = models.AutoField(primary_key=True)
    datetime = models.DateTimeField()
    state = models.CharField(max_length=1, choices=WEATHER_STATES)



