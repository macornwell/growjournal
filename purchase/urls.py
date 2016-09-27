from django.conf.urls import url
from core.urls import create_crud_urls
from purchase.views import StoreCRUDView, PurchaseCRUDView

urlpatterns = []
urlpatterns += create_crud_urls(StoreCRUDView())
urlpatterns += create_crud_urls(PurchaseCRUDView())

