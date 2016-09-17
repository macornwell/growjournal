from django.utils import timezone
from django.db import models
from core.models import BaseUserActivityModel, get_objects_with_datetime_property_on_given_date
from core.utils import get_local_time_formatted

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
    ('t', 'Frost'),
    ('n', 'Snow'),
)

WEATHER_STATES_DICT = {key: value for (key, value) in WEATHER_STATES}


class TemperatureReading(BaseUserActivityModel):
    temperature_reading_id = models.AutoField(primary_key=True)
    value = models.DecimalField(decimal_places=2, max_digits=8)
    datetime = models.DateTimeField(default=timezone.now)
    unit = models.CharField(max_length=1, choices=TEMPERATURE_UNITS, default=TEMPERATURE_UNITS[0][0])

    def __str__(self):
        return '{0} - {1}{2}\u00B0'.format(get_local_time_formatted(self.datetime), self.value, self.unit)

    @staticmethod
    def get_readings_by_date(date):
        return get_objects_with_datetime_property_on_given_date(TemperatureReading, date)


class WeatherReading(BaseUserActivityModel):
    weather_reading_id = models.AutoField(primary_key=True)
    datetime = models.DateTimeField(default=timezone.now)
    state = models.CharField(max_length=1, choices=WEATHER_STATES)
    temperature = models.DecimalField(decimal_places=2, max_digits=8)
    unit = models.CharField(max_length=1, choices=TEMPERATURE_UNITS, default=TEMPERATURE_UNITS[0][0])

    def __str__(self):
        return '{0} - {1} {2}'.format(get_local_time_formatted(self.datetime), self.temperature, WEATHER_STATES_DICT[self.state])

    @staticmethod
    def get_readings_by_date(date):
        return get_objects_with_datetime_property_on_given_date(WeatherReading, date)






