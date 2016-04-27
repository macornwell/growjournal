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

