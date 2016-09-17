from django.conf.urls import url
from observations.views import add_observation

urlpatterns = [
    url('^add/observation$', name='add_observation', view=add_observation),
]