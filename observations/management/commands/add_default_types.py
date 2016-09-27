from django.core.management import BaseCommand
from observations.models import ObservationType, DEFAULT_TYPES, DEFAULT_PLANT_OBSERVATION_TYPES
from taxonomy.models import Kingdom

class Command(BaseCommand):
    help = """
    Ensures all default Types have been added to the database.
           """

    def handle(self, *args, **options):
        for type in DEFAULT_TYPES:
            a, added = ObservationType.objects.get_or_create(name=type)
            if added:
                print('Added {0} Observation Type.'.format(a))
        kingdom = Kingdom.get_plant_kingdom()
        for type in DEFAULT_PLANT_OBSERVATION_TYPES:
            a, added = ObservationType.objects.get_or_create(name=type, kingdom_specific=kingdom)
            if added:
                print('Added {0} Plant Observation Type.'.format(a))


