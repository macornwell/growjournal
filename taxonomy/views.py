from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from core.views import list_model_view, ListEntry, WIZARD_FORM_TEMPLATE, get_back_to_settings_string
from taxonomy.models import SiteInventory, Genus, Kingdom, Species, Variety
from taxonomy.forms import GenusForm, SpeciesForm, VarietyForm
from taxonomy.templatetags.taxonomy_tags import order_genus
from taxonomy.services import is_using_latin


"""
Site Inventory
"""

def add_site_inventory(request):
    return

def list_site_inventory(request):
    kingdomToGenusToInventorySection = {}
    for inventory in SiteInventory.objects.get_inventory_for_user(request.user):
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
    latinName = request.POST['latin-name']
    if not variety:
        variety = Variety()
    variety.name = name
    variety.latin_name = latinName
    variety.species = Species.objects.get(species_id=speciesID)
    variety.save()
    return redirect('setup')


def edit_variety(request):
    pass


def list_variety(request):
    pass


