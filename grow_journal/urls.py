from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.contrib.auth.views import login
from grow_journal import settings
from rest_framework import routers
import core.urls as CoreUrls
import observations.urls as ObservationUrls
import taxonomy.urls as TaxonomyUrls
from grow_journal.views import home, setup, settings_view

router = routers.DefaultRouter()


"""
url(r'^(?P<page>-?\d+)/$', home_with_page, name='home'),
#url(r'^(?P<page>.+)/$', home, name='home'),
#url(r'^work-site/$', worksite, name='work-site'),
"""
urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^setup$', setup, name='setup'),
    url(r'^setup/settings$', settings_view, name='settings'),
    url(r'^admin/', admin.site.urls, name='admin'),
    url(r'^login/$', login, {'template_name': 'admin/login.html'})
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += CoreUrls.urlpatterns
urlpatterns += ObservationUrls.urlpatterns
urlpatterns += TaxonomyUrls.urlpatterns

###################
# Rest Framework
###################

urlpatterns += [
    url(r'^api/', include(router.urls), name='api'),
    #url(r'^api/log_message', post_log_messages_json, name='log_message'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]

