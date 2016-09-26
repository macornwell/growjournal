from django.contrib.auth.models import User
from django.db import models
from core.models import BaseModel,  Site
from geography.models import Location
from taxonomy.managers import SiteInventoryManager, UserTaxonomySettingsManager, KingdomManager, GenusManager, LifeFormManager

PLANT_KINGDOM_NAME = 'Plant Kingdom'
ANIMAL_KINGDOM_NAME = 'Animal Kingdom'

DWARFING_CHOICES = (
    ('vd', 'Very-Dwarfing'),
    ('d', 'Dwarf'),
    ('sd', 'Semi-Dwarf'),
    ('f', 'Full-Size')
)


def get_animal_kingdom():
    return Kingdom.objects.get_or_create(name=ANIMAL_KINGDOM_NAME, latin_name='Animalia')[0]


def get_plant_kingdom():
    return Kingdom.objects.get_or_create(name=PLANT_KINGDOM_NAME, latin_name='Plantae')[0]


def get_unknown_rootstock():
    """
    unknownRootstock = Rootstock.objects.filter(denormalized_name='Unknown').first()
    if not unknownRootstock:
        plantKingdom, created = Kingdom.objects.get_or_create(name='Plant Kingdom', latin_name='Plantae')
        unknownGenus, created = Genus.objects.get_or_create(name='Unknown', latin_name='Unknown', kingdom_id=plantKingdom.kingdom_id)
        unknownSpecies, created = Species.objects.get_or_create(name='Unknown', latin_name='Unknown', genus=unknownGenus)
        unknownVariety, created = Variety.objects.get_or_create(name='Unknown', latin_name='Unknown', species=unknownSpecies)
        unknownRootstock, created = Rootstock.objects.get_or_create(variety=unknownVariety, denormalized_name=unknownVariety.name)
    """
    unknownRootstock = ""
    return unknownRootstock


class UserTaxonomySettings(BaseModel):
    objects = UserTaxonomySettingsManager()
    user = models.OneToOneField(User)
    use_latin_name = models.BooleanField(default=True)


class Kingdom(BaseModel):
    objects = KingdomManager()
    kingdom_id = models.AutoField(primary_key=True)
    latin_name = models.CharField(max_length=30, unique=True)
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.latin_name


class Genus(BaseModel):
    objects = GenusManager()
    genus_id = models.AutoField(primary_key=True)
    kingdom = models.ForeignKey(Kingdom)
    latin_name = models.CharField(max_length=30, unique=True)
    name = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.latin_name or self.name


class Species(BaseModel):
    species_id = models.AutoField(primary_key=True)
    genus = models.ForeignKey(Genus)
    latin_name = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    origin_location = models.ForeignKey(Location, blank=True, null=True)

    def __str__(self):
        return self.latin_name or self.name

    class Meta:
        unique_together = (("genus", "name"),)

    def save(self, *args, **kwargs):
        super(Species, self).save(*args, **kwargs)
        LifeForm.objects.get_or_create_from_species(self)


class Variety(BaseModel):
    variety_id = models.AutoField(primary_key=True)
    species = models.ForeignKey(Species)
    name = models.CharField(max_length=40)
    name_denormalized = models.CharField(max_length=50, blank=True)
    latin_name = models.CharField(max_length=50, blank=True)
    parent_a = models.ForeignKey('Variety', blank=True, null=True, related_name='first_children')
    parent_b = models.ForeignKey('Variety', blank=True, null=True, related_name='second_children')
    history = models.TextField(blank=True, null=True)
    origin_location = models.ForeignKey(Location, blank=True, null=True)
    origin_year = models.IntegerField(blank=True, null=True)
    chromosome_count = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        unique_together = (("species", "name"),)

    def save(self, *args, **kwargs):
        if not self.latin_name:
            self.latin_name = "{0} '{1}'".format(self.species.latin_name, self.name)
        if not self.name_denormalized:
            self.name_denormalized = '{0} {1}'.format(self.name, self.species.name)
        super(BaseModel, self).save(*args, **kwargs)
        LifeForm.objects.get_or_create_from_variety(self)


class Rootstock(BaseModel):
    rootstock_id = models.AutoField(primary_key=True)
    variety = models.OneToOneField(Variety)
    denormalized_name = models.CharField(max_length=30)
    dwarfing = models.CharField(max_length=2, choices=DWARFING_CHOICES)

    def save(self, *args, **kwargs):
        if self.variety.species.kingdom.name != PLANT_KINGDOM_NAME:
            raise Exception('Only Plants can be rootstocks.')
        super(BaseModel, self).save(*args, **kwargs)


class LifeForm(BaseModel):
    objects = LifeFormManager()
    life_form_id = models.AutoField(primary_key=True)
    kingdom = models.ForeignKey(Kingdom)
    genus = models.ForeignKey(Genus)
    species = models.ForeignKey(Species)
    variety = models.ForeignKey(Variety, blank=True, null=True)
    rootstock = models.ForeignKey(Rootstock, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True)
    latin_name = models.CharField(max_length=50, blank=True)

    class Meta:
        unique_together = (('kingdom', 'genus', 'species', 'variety', 'rootstock'),)

    def save(self, *args, **kwargs):
        self._perform_validation()
        self._perform_denormalization()
        super(BaseModel, self).save(*args, **kwargs)
        self._perform_additional_saving()

    def _perform_validation(self):
        if self.genus.kingdom != self.kingdom:
            raise Exception('The kingdom for the genus does not match the kingdom selected.')
        if self.species.genus.kingdom != self.kingdom:
            raise Exception('The kingdom for the species does not match the kingdom selected.')
        if self.species.genus != self.genus:
            raise Exception('The genus for the species does not match the genus selected.')
        if self.variety:
            if self.variety.species != self.species:
                raise Exception('The species of the variety does not match the species selected.')
        if self.rootstock:
            if self.kingdom.name != PLANT_KINGDOM_NAME:
                raise Exception('Only Plants can be grafted.')
            if not self.variety:
                raise Exception('A rootstock requires a variety.')

    def _perform_denormalization(self):
        if not self.name:
            if self.variety:
                self.name = self.variety.name
            else:
                self.name = self.species.name
        if not self.latin_name:
            self.latin_name = self.species.latin_name
            if self.variety:
                self.latin_name = "{0} '{1}'".format(self.latin_name, self.name)

    def _perform_additional_saving(self):
        if self.rootstock:
            if LifeForm.objects.has_variety(self.variety_id):
                pass

    def __str__(self):
        line = ''
        if self.variety:
            line += self.variety.name + ' ('

        line += self.species.name
        if self.variety:
            line += ')'
        if self.rootstock:
            line += ' grafted to {0}'.format(self.rootstock.denormalized_name)
        return line


class SiteInventory(BaseModel):
    objects = SiteInventoryManager()
    site_inventory_id = models.AutoField(primary_key=True)
    site = models.ForeignKey(Site)
    life_form = models.ForeignKey(LifeForm)
    count = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = ('site', 'life_form')

    def __str__(self):
        return self.life_form.__str__()


