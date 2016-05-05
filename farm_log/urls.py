from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from farm_log import settings
from farm_log.views import home, worksite
from rest_framework import routers
import core.urls as CoreUrls
import observations.urls as ObservationUrls
import work.urls as WorkUrls
import livestock.urls as LivestockUrls
import plants.urls as PlantsUrls

router = routers.DefaultRouter()


urlpatterns = [
    url(r'^$', home),
    url(r'^work-site/$', worksite, name='work-site'),
    url(r'^admin-site/', admin.site.urls, name='admin'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += CoreUrls.urlpatterns
urlpatterns += ObservationUrls.urlpatterns
urlpatterns += WorkUrls.urlpatterns
urlpatterns += LivestockUrls.urlpatterns
urlpatterns += PlantsUrls.urlpatterns

urlpatterns += [
    url(r'^api/', include(router.urls), name='api'),
    #url(r'^api/log_message', post_log_messages_json, name='log_message'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

