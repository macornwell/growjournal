from django.conf.urls import url
from core.views import change_site, SiteCRUDView, UnitCRUDView, ProjectCRUDView

def create_crud_urls(crudView):
    list = [
        url(r'^{0}/$'.format(crudView.plural), name=crudView.get_list_url(), view=crudView.list),
        url(r'^{0}/add'.format(crudView.plural), name=crudView.get_add_url(), view=crudView.add),
        url(r'^{0}/edit/(?P<modelID>\d+)'.format(crudView.plural), name=crudView.get_edit_url(), view=crudView.edit),
    ]
    return list


urlpatterns = [
    url(r'^setup/sites/change/(?P<siteID>\d+)', name='change_site', view=change_site),
]

urlpatterns += create_crud_urls(SiteCRUDView())
urlpatterns += create_crud_urls(UnitCRUDView())
urlpatterns += create_crud_urls(ProjectCRUDView())
