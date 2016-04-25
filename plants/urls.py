from django.conf.urls import url
from plants.views import add_harvest, add_watering, add_plant_productivity, add_bloom, add_resource

urlpatterns = [
    url('^add/plants/resource', name='add_resource', view=add_resource),
    url('^add/plants/harvest', name='add_harvest', view=add_harvest),
    url('^add/plants/watering', name='add_watering', view=add_watering),
    url('^add/plants/productivity', name='add_plant_productivity', view=add_plant_productivity),
    url('^add/plants/bloom', name='add_bloom', view=add_bloom),
]