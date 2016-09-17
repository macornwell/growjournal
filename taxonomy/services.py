from taxonomy.models import LifeForm


def get_or_create_lifeform(kingdom, genus, species, variety=None):
    return LifeForm.objects.get_or_create(kingdom=kingdom, genus=genus, species=species, variety=variety)

