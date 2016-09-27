from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from core.views import CRUDView
from core.services import get_active_site
from purchase.models import Store, PurchaseEvent
from purchase.forms import StoreForm, PurchaseForm


class StoreCRUDView(CRUDView):
    model_type = Store
    form_type = StoreForm
    singular = 'Store'
    plural = 'Stores'

    def get_model(self, modelID):
        return Store.objects.get(store_id=modelID)

    def get_id(self, model):
        return model.store_id

    def post(self, request, model=None):
        name = request.POST['name']
        if not model:
            model = Store()
        model.name = name
        model.save()
        return self.list(request)


class PurchaseCRUDView(CRUDView):
    model_type = PurchaseEvent
    form_type = PurchaseForm
    singular = 'Purchase'
    plural = 'Purchases'
    back_list_url = reverse_lazy('home')

    def get_model(self, modelID):
        return PurchaseEvent.objects.get(purchase_event_id=modelID)

    def get_id(self, model):
        return model.purchase_event_id

    def create_form(self, request):
        form = PurchaseForm()
        site = get_active_site(request.user)
        form.fill_projects(site)
        return form

    def post(self, request, model=None):
        raise NotImplemented()
        name = request.POST['name']
        if not model:
            model = PurchaseEvent()
        model.name = name
        model.save()
        return self.list(request)