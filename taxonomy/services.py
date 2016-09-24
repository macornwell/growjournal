from taxonomy.models import LifeForm, Kingdom, Genus, Species, Variety, SiteInventory, UserTaxonomySettings


def get_or_create_lifeform(kingdom, genus, species, variety=None):
    return LifeForm.objects.get_or_create(kingdom=kingdom, genus=genus, species=species, variety=variety)


def is_using_latin(user):
    return UserTaxonomySettings.objects.get_settings(user).use_latin_name


def get_taxonomy_name(taxonomy, useLatin):
    name = ''
    if useLatin:
        if isinstance(taxonomy, SiteInventory):
            name = taxonomy.life_form.latin_name
        else:
            name = taxonomy.latin_name
    else:
        if isinstance(taxonomy, SiteInventory):
            name = taxonomy.life_form.name
        else:
            name = taxonomy.name
            if isinstance(taxonomy, Variety):
                name = taxonomy.name_denormalized
    return name
