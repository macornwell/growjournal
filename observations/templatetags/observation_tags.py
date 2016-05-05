from django import template
from observations.models import WEATHER_STATES_DICT

register = template.Library()

WEATHER_STATE_TO_GLYPH = {
    's': 'wi-day-sunny',
    'p': 'wi-day-sunny-overcast',
    'c': 'wi-cloud',
    'o': 'wi-cloudy',
    'r': 'wi-day-rain',
    'f': 'wi-snowflake-cold',
    't': 'wi-stars',
    'n': 'wi-snow',
}



@register.filter
def get_weather_symbol(weatherReading):
    return 'wi {}'.format(WEATHER_STATE_TO_GLYPH[weatherReading.state])


@register.filter
def get_weather_state_in_full(weatherReading):
    return WEATHER_STATES_DICT[weatherReading.state]

@register.filter
def get_high_low_string(temperatureReadings):
    value = ''
    if temperatureReadings:
        low = min(temperatureReadings, key=lambda reading: reading.value)
        high = max(temperatureReadings, key=lambda reading: reading.value)
        if low == high:
            value = '{0}\u00B0{1}'.format(low.value, low.unit)
        else:
            value = 'High: {0}\u00B0{1} - Low: {2}\u00B0{1}'.format(high.value, high.unit, low.value)
    return value
