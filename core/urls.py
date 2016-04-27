from django.conf.urls import url
from core.views import add_note

urlpatterns = [
    url('^add/core/note', name='add_note', view=add_note),
]