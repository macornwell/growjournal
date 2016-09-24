from django.conf.urls import url
from core.views import add_feedback, add_site, change_site, edit_site, list_sites

urlpatterns = [
    url('^add/core/feedback', name='add_feedback', view=add_feedback),
    url(r'^setup/sites/change/(?P<siteID>\d+)', name='change_site', view=change_site),
    url(r'^sites/$', name='sites', view=list_sites),
    url('^sites/add', name='add_site', view=add_site),
    url(r'^sites/edit/(?P<siteID>\d+)', name='edit_site', view=edit_site),
]