from django.conf import settings

"""
    Weather Settings
WEATHER_DATA = {'DJANGO_USERNAME':{
'wunder_key':'WUNDERGROUND_KEY',
'city':'CITY_TO_SEARCH',
'state':'STATE_TO_SEARCH',
}}


"""

default_data = {}
WEATHER_DATA = getattr(settings, 'WEATHER_DATA', default_data)
