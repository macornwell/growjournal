from django.conf.urls import url
from taxonomy.views import list_site_inventory, add_site_inventory, list_genus, add_genus, edit_genus, list_species, add_species, edit_species, add_variety, list_variety, edit_variety


urlpatterns = [
    url(r'^site-inventory/$', name='list_site_inventory', view=list_site_inventory),
    url(r'^site-inventory/add/$', name='add_site_inventory', view=add_site_inventory),

    url(r'^genus/$', name='list_genus', view=list_genus),
    url(r'^genus/add/$', name='add_genus', view=add_genus),
    url(r'^genus/edit/(?P<genusID>\d+)$', name='edit_genus', view=edit_genus),

    url(r'^species/$', name='list_species', view=list_species),
    url(r'^species/add/$', name='add_species', view=add_species),
    url(r'^species/edit/(?P<speciesID>\d+)$', name='edit_species', view=edit_species),

    url(r'^variety/$', name='list_variety', view=list_variety),
    url(r'^variety/add/$', name='add_variety', view=add_variety),
    url(r'^variety/edit/(?P<varietyID>\d+)$', name='edit_variety', view=edit_variety),
]
