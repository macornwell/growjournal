from django.core.management import BaseCommand
from taxonomy.models import Kingdom, Genus, Species, Variety, Rootstock, LifeForm

class Command(BaseCommand):
    help = """
    Makes sure that all expected LifeForms have been created.
           """

    def handle(self, *args, **options):
        for species in Species.objects.all():
            lifeForm = LifeForm.objects.filter(species=species, variety=None, rootstock=None).first()
            if not lifeForm:
                print('Saving LifeForm for Species: {0}'.format(species.latin_name))
                lifeForm = LifeForm(kingdom=species.genus.kingdom, genus=species.genus, species=species)
                lifeForm.save()
        for variety in Variety.objects.all():
            lifeForm = LifeForm.objects.filter(species=variety.species, variety=variety, rootstock=None).first()
            if not lifeForm:
                print('Saving LifeForm for Variety: {0}'.format(variety.name_denormalized))
                lifeForm = LifeForm(kingdom=variety.species.genus.kingdom, genus=variety.species.genus, species=variety.species, variety=variety)
                lifeForm.save()






