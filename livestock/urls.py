from django.conf.urls import url
from livestock.views import add_egg_collection, add_animal_report

urlpatterns = [
    url('^add/livestock/eggs', name='add_egg_collection', view=add_egg_collection),
    url('^add/livestock/report', name='add_animal_report', view=add_animal_report),
]