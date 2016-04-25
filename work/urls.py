from django.conf.urls import url
from work.views import add_work_completed

urlpatterns = [
    url('^add/work/work_completed', name='add_work_completed', view=add_work_completed),
]
