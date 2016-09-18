from django.conf.urls import url
from core.views import add_feedback, add_site

urlpatterns = [
    url('^add/core/feedback', name='add_feedback', view=add_feedback),
    url('^setup/sites/add', name='add_site', view=add_site),
]