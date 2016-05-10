from django.conf.urls import url
from core.views import add_feedback

urlpatterns = [
    url('^add/core/feedback', name='add_feedback', view=add_feedback),
]