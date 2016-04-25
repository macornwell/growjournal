from django.conf.urls import url
from livestock.views import add_egg_collection

urlpatterns = [
    url('^add/livestock/eggs', name='add_egg_collection', view=add_egg_collection),
]