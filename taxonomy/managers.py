from django.db import models


class SiteInventoryManager(models.Manager):
    def get_inventory_for_user(self, user):
        return super(SiteInventoryManager, self).get_queryset().filter(user=user)


class LifeFormManager(models.Manager):

    def get_or_create_from_species(self, species):
        lifeForm = super(LifeFormManager, self).get_or_create(kingdom=species.genus.kingdom, genus=species.genus, species=species, name=species.name, latin_name=species.latin_name)[0]
        return lifeForm


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


class GenusManager(models.Manager, NameAndLatinNameManagerMixin):

    def get_genus_by_kingdom(self, kingdom):
        return super(GenusManager, self).get_queryset().filter(kingdom=kingdom)



