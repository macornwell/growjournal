from django.conf.urls import url
from core.urls import create_crud_urls
from taxonomy.views import GenusCRUDView, SiteInventoryCRUDView, \
    SpeciesCRUDView, VarietyCRUDView, life_form_search


urlpatterns = [
    url(r'^lifeform/query/(?P<query>[a-z\dA-Z]+)', name='life_form_search', view=life_form_search),
    ]

urlpatterns += create_crud_urls(SiteInventoryCRUDView())
urlpatterns += create_crud_urls(GenusCRUDView())
urlpatterns += create_crud_urls(SpeciesCRUDView())
urlpatterns += create_crud_urls(VarietyCRUDView())
