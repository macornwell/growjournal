from django.core.management import BaseCommand
from taxonomy.models import Kingdom, Genus, Species, Cultivar, Rootstock, LifeForm

class Command(BaseCommand):
    help = """
    Makes sure that all expected LifeForms have been created.
           """

    def handle(self, *args, **options):
        for species in Species.objects.all():
            lifeForm = LifeForm.objects.filter(species=species, cultivar=None, rootstock=None).first()
            if not lifeForm:
                print('Saving LifeForm for Species: {0}'.format(species.latin_name))
                lifeForm = LifeForm(kingdom=species.genus.kingdom, genus=species.genus, species=species)
                lifeForm.save()
        for cultivar in Cultivar.objects.all():
            lifeForm = LifeForm.objects.filter(species=cultivar.species, cultivar=cultivar, rootstock=None).first()
            if not lifeForm:
                print('Saving LifeForm for Cultivar: {0}'.format(cultivar.name_denormalized))
                lifeForm = LifeForm(kingdom=cultivar.species.genus.kingdom, genus=cultivar.species.genus, species=cultivar.species, cultivar=cultivar)
                lifeForm.save()






