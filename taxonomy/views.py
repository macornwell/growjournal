from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.forms.models import model_to_dict
from django.http import JsonResponse
from core.models import Site
from core.services import get_active_site
from taxonomy.models import SiteInventory, Genus, Kingdom, Species, Variety, LifeForm
from taxonomy.forms import GenusForm, SpeciesForm, VarietyForm, SiteInventoryForm
from taxonomy.services import is_using_latin

from django_wizard_crud_view.views import CRUDView, ListEntry

"""
Site Inventory
"""

class SiteInventoryCRUDView(CRUDView):
    model_type = SiteInventory
    form_type = SiteInventoryForm
    singular = "Site Inventory"
    plural = "Site Inventory"
    list_template_path = 'taxonomy/list-site-inventory.html'

    def get_model(self, modelID):
        return SiteInventory.objects.get(site_inventory_id=modelID)

    def get_id(self, model):
        return model.site_inventory_id

    def post(self, request, model=None):
        count = request.POST['count'] or 1
        lifeFormID = request.POST['life-form']
        siteID = request.POST['site']
        if not model:
            model = SiteInventory()
        model.count = count
        model.life_form = LifeForm.objects.get(life_form_id=lifeFormID)
        model.site = Site.objects.get(site_id=siteID)
        model.save()
        return self.list(request)

    def list(self, request):
        kingdomToGenusToInventorySection = {}
        for inventory in SiteInventory.objects.get_inventory_for_site(get_active_site(request.user)):
            life = inventory.life_form
            if life.kingdom not in kingdomToGenusToInventorySection:
                kingdomToGenusToInventorySection[life.kingdom] = {}
            innerDict = kingdomToGenusToInventorySection[life.kingdom]
            if life.genus not in kingdomToGenusToInventorySection[life.kingdom]:
                kingdomToGenusToInventorySection[life.kingdom][life.genus] = []
            modelList = kingdomToGenusToInventorySection[life.kingdom][life.genus]
            modelList.append(inventory)

        return self.list_model_view(request, self.singular, reverse(self.get_add_url()), self.singular, self.plural, kingdomToGenusToInventorySection, backButtonUrl=reverse('setup'))




"""
Genus
"""

class GenusCRUDView(CRUDView):
    model_type = Genus
    form_type = GenusForm
    singular = "Genus"
    plural = "Genus"
    list_model_template_path ='taxonomy/taxonomy-name.html',

    def get_model(self, modelID):
        return Genus.objects.get(genus_id=modelID)

    def get_id(self, model):
        return model.genus_id

    def get_back_list_url(self):
        return reverse('setup')

    def get_list_of_models(self, request):
        isLatin = is_using_latin(request.user)
        data = Genus.objects.order_by_name(isLatin)
        return data

    def post(self, request, model=None):
        kingdomName = request.POST['kingdom']
        name = request.POST['name']
        latinName = request.POST['latin-name']
        if not model:
            model = Genus()
        model.name = name
        model.latin_name = latinName
        model.kingdom = Kingdom.objects.get_kingdom_by_name(kingdomName)
        model.save()
        return self.list(request)


class SpeciesCRUDView(CRUDView):
    model_type = Species
    form_type = SpeciesForm
    singular = "Species"
    plural = "Species"

    def get_model(self, modelID):
        return Species.objects.get(species_id=modelID)

    def get_id(self, model):
        return model.species_id

    def get_back_list_url(self):
        return reverse('setup')

    def post(self, request, model=None):
        genusID = request.POST['genus']
        name = request.POST['name']
        latinName = request.POST['latin-name']
        if not model:
            model = Species()
        model.name = name
        model.latin_name = latinName
        model.genus = Genus.objects.get(genus_id=genusID)
        model.save()
        return redirect('setup')

class VarietyCRUDView(CRUDView):
    model_type = Variety
    form_type = VarietyForm
    singular = "Variety"
    plural = "Varieties"

    def get_model(self, modelID):
        return Variety.objects.get(variety_id=modelID)

    def get_id(self, model):
        return model.genus_id

    def get_back_list_url(self):
        return reverse('setup')

    def post(self, request, model=None):
        speciesID = request.POST['species']
        name = request.POST['name']
        if not model:
            model = Variety()
        model.name = name
        model.species = Species.objects.get(species_id=speciesID)
        model.save()
        return redirect('setup')



def life_form_search(request, query):
    query = query.lower()
    limit = 20
    results = LifeForm.objects.search_all(query, limit)
    data = {}
    for r in results:
        species = {
            'species_id': r.species.species_id,
            'name': r.species.latin_name,
            'latin_name': r.species.name,
        }
        data[r.life_form_id] = {
            'life_form_id': r.life_form_id,
            'name': r.name,
            'latin_name': r.latin_name,
            'variety': '',
            'rootstock': '',
            'species': species,
        }
        if r.variety:
            data[r.life_form_id]['variety'] = r.variety.name
        if r.rootstock:
            data[r.life_form_id]['rootstock'] = r.rootstock.name
    return JsonResponse(data)


