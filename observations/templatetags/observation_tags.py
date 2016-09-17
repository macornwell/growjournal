from django import template
from observations.models import WEATHER_STATES_DICT
from django.utils.html import format_html
from django.utils.safestring import mark_safe
import pytz
import datetime
from grow_journal.settings import DEFAULT_TIME_ZONE

register = template.Library()

today = datetime.datetime.now()
TIMEZONE_OFFSET = pytz.timezone(DEFAULT_TIME_ZONE).utcoffset(today).total_seconds()/60/60

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
def get_high_low_string(weatherReadings):
    value = ''
    if weatherReadings:
        low = min(weatherReadings, key=lambda reading: reading.temperature)
        high = max(weatherReadings, key=lambda reading: reading.temperature)
        if low == high:
            value = '{0}\u00B0{1}'.format(low.temperature, low.unit)
        else:
            value = 'High: {0}\u00B0{1} - Low: {2}\u00B0{1}'.format(high.temperature, high.unit, low.temperature)
    return value

@register.filter
def get_weather_html(weatherReadings):
    low = min(weatherReadings, key=lambda x: x.temperature)
    high = max(weatherReadings, key=lambda x: x.temperature)
    if high == low:
        high = None
    html = _get_formatted_weather_string(low, 'Low') + _get_formatted_weather_string(high, 'High')
    return mark_safe(format_html(html))

def _get_formatted_weather_string(reading, timeOfDayString):
    formattedString = """<span class="col-xs-6">
                            {0}:
                        """.format(timeOfDayString)
    if reading:
        temp = ' {0}\u00B0{1} '.format(reading.temperature, reading.unit)
        details = """ <span>{0}</span>
        <span aria-hidden="true"
                class="weather-icon {1}"></span>
                """
        formattedString += details.format(temp, get_weather_symbol(reading))
    return formattedString + '</span>'

def _get_weather_reading_between_times(readings, beginHour, endHour):
    inOrder = sorted(readings, key=lambda x: x.datetime.hour)
    for reading in inOrder:
        dateTime = reading.datetime
        hour = dateTime.hour + TIMEZONE_OFFSET
        if hour >= beginHour and hour <= endHour:
            return reading
    return None
