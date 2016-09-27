from django.db import models
from django.db.models import Q

PLANT_KINGDOM_NAME = 'Plant Kingdom'
ANIMAL_KINGDOM_NAME = 'Animal Kingdom'


class SiteInventoryManager(models.Manager):
    def get_inventory_for_site(self, site):
        return super(SiteInventoryManager, self).get_queryset().filter(site=site)


class LifeFormManager(models.Manager):

    def get_or_create_from_species(self, species):
        lifeForm = super(LifeFormManager, self).get_or_create(kingdom=species.genus.kingdom, genus=species.genus, species=species, name=species.name, latin_name=species.latin_name)[0]
        return lifeForm

    def get_or_create_from_variety(self, variety):
        lifeForm = super(LifeFormManager, self).get_or_create(kingdom=variety.species.genus.kingdom, genus=variety.species.genus, species=variety.species, name=variety.species.name, latin_name=variety.species.latin_name)[0]
        lifeForm = super(LifeFormManager, self).get_or_create(kingdom=variety.species.genus.kingdom, genus=variety.species.genus, species=variety.species, name=variety.name, latin_name=variety.latin_name, variety=variety)[0]
        return lifeForm

    def get_all_life_forms_for_species(self, species):
        return super(LifeFormManager, self).get_queryset().filter(species_id=species.species_id)

    def get_all_life_forms_for_variety(self, variety):
        return super(LifeFormManager, self).get_queryset().filter(variety_Id=variety.variety_id)

    def get_all_life_forms_for_rootstock(self, rootstock):
        return super(LifeFormManager, self).get_queryset().filter(rootstock_id=rootstock.rootstock_id)

    def search_all(self, query, limit=20):
        return super(LifeFormManager, self).get_queryset().filter(Q(name__icontains=query) | Q(latin_name__icontains=query) | Q(variety__isnull=False, variety__name__icontains=query)).distinct()[:20]


class UserTaxonomySettingsManager(models.Manager):

    def get_settings(self, user):
        return super(UserTaxonomySettingsManager, self).get_queryset().get_or_create(user=user)[0]


class NameAndLatinNameManagerMixin:

    def order_by_name(self, isUsingLatin):
        if isUsingLatin:
            return self.get_queryset().order_by('latin_name')
        else:
            return self.get_queryset().order_by('name')


class KingdomManager(models.Manager, NameAndLatinNameManagerMixin):

    def get_kingdom_by_name(self, name):
        return super(KingdomManager, self).get_queryset().filter(name=name).first()

    def get_animal_kingdom(self):
        return self.get_or_create(name=ANIMAL_KINGDOM_NAME, latin_name='Animalia')[0]

    def get_plant_kingdom(self):
        return self.get_or_create(name=PLANT_KINGDOM_NAME, latin_name='Plantae')[0]


class GenusManager(models.Manager, NameAndLatinNameManagerMixin):

    def get_genus_by_kingdom(self, kingdom):
        return super(GenusManager, self).get_queryset().filter(kingdom=kingdom)


