from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.forms.models import model_to_dict
from django.http import JsonResponse
from core.models import Site
from core.views import list_model_view, ListEntry, WIZARD_FORM_TEMPLATE, get_back_to_settings_string
from core.services import get_active_site
from taxonomy.models import SiteInventory, Genus, Kingdom, Species, Variety, LifeForm
from taxonomy.forms import GenusForm, SpeciesForm, VarietyForm, SiteInventoryForm
from taxonomy.services import is_using_latin


"""
Site Inventory
"""


def add_site_inventory(request):
    data = {}
    if request.POST:
        return post_site_inventory(request)
    form = SiteInventoryForm()
    data['form'] = form
    return render(request, WIZARD_FORM_TEMPLATE, data)


def post_site_inventory(request, model=None):
    count = request.POST['count'] or 1
    lifeFormID = request.POST['life-form']
    siteID = request.POST['site']
    if not model:
        model = SiteInventory()
    model.count = count
    model.life_form = LifeForm.objects.get(life_form_id=lifeFormID)
    model.site = Site.objects.get(site_id=siteID)
    model.save()
    return list_site_inventory(request)


def list_site_inventory(request):
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

    return list_model_view(request, 'Site Inventory', reverse('add_site_inventory'), 'Site Inventory', 'Site Inventories', kingdomToGenusToInventorySection, template='taxonomy/list-site-inventory.html', backButtonUrl=get_back_to_settings_string())




"""
Genus
"""

def edit_genus(request, genusID):
    data = {}
    genus = Genus.objects.filter(genus_id=genusID).first()
    if request.POST:
        if 'delete-button' in request.POST:
            return delete_genus(request, genus)
        return post_genus(request, genus)
    form = GenusForm()
    form.apply_instance(genus)
    data['form'] = form
    data['is_editing_model'] = True
    return render(request, WIZARD_FORM_TEMPLATE, data)


def delete_genus(request, genus):
    genus.delete()
    return list_genus(request)


def list_genus(request):
    isLatin = is_using_latin(request.user)
    data = Genus.objects.order_by_name(isLatin)
    entries = []
    for genus in data:
        entries.append(ListEntry(model=genus, edit_url=reverse('edit_genus', kwargs={'genusID': genus.genus_id})))
    return list_model_view(request, 'Genus', reverse('add_genus'), 'Genus', 'Genuses', entries, modelTemplatePath='taxonomy/taxonomy-name.html', backButtonUrl=get_back_to_settings_string())


def add_genus(request):
    data = {}
    if request.POST:
        return post_genus(request)
    form = GenusForm()
    data['form'] = form
    return render(request, WIZARD_FORM_TEMPLATE, data)


def post_genus(request, genus=None):
    kingdomName = request.POST['kingdom']
    name = request.POST['name']
    latinName = request.POST['latin-name']
    if not genus:
        genus = Genus()
    genus.name = name
    genus.latin_name = latinName
    genus.kingdom = Kingdom.objects.get_kingdom_by_name(kingdomName)
    genus.save()
    return list_genus(request)


def add_species(request):
    data = {}
    if request.POST:
        return post_species(request)
    form = SpeciesForm()
    data['form'] = form
    return render(request, WIZARD_FORM_TEMPLATE, data)


def post_species(request, species=None):
    genusID = request.POST['genus']
    name = request.POST['name']
    latinName = request.POST['latin-name']
    if not species:
        species = Species()
    species.name = name
    species.latin_name = latinName
    species.genus = Genus.objects.get(genus_id=genusID)
    species.save()
    return redirect('setup')


def list_species(request):
    pass


def edit_species(request, speciesID):
    pass


def add_variety(request):
    data = {}
    if request.POST:
        return post_variety(request)
    form = VarietyForm()
    data['form'] = form
    return render(request, WIZARD_FORM_TEMPLATE, data)


def post_variety(request, variety=None):
    speciesID = request.POST['species']
    name = request.POST['name']
    #latinName = request.POST['latin-name']
    if not variety:
        variety = Variety()
    variety.name = name
    #variety.latin_name = latinName
    variety.species = Species.objects.get(species_id=speciesID)
    variety.save()
    return redirect('setup')


def edit_variety(request):
    pass


def list_variety(request):
    pass


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


