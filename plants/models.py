from django.db import models
from django.utils import timezone
from core.models import BaseModel, BaseUserActivityModel, Project, Unit, get_objects_with_datetime_property_on_given_date
from core.utils import get_local_time_formatted
from plants.mixins import SpeciesOrCultivarMixin


"""

General Models

"""


class Genius(BaseModel):
    genius_id = models.AutoField(primary_key=True)
    latin_name = models.CharField(max_length=30, unique=True, blank=True)
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.latin_name or self.name


class Species(BaseModel):
    species_id = models.AutoField(primary_key=True)
    genius = models.ForeignKey(Genius)
    latin_name = models.CharField(max_length=30, blank=True, null=True)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.latin_name or self.name

    class Meta:
        unique_together = (("genius", "name"),)


class Cultivar(BaseModel):
    plant_id = models.AutoField(primary_key=True)
    species = models.ForeignKey(Species)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

    class Meta:
        unique_together = (("species", "name"),)


class Resource(BaseModel, SpeciesOrCultivarMixin):
    resource_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, unique=True)
    species = models.ForeignKey(Species, blank=True, null=True)
    cultivar = models.ForeignKey(Cultivar, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

"""

Work

"""


class Harvest(BaseUserActivityModel):
    harvest_id = models.AutoField(primary_key=True)
    resource = models.ForeignKey(Resource)
    datetime = models.DateTimeField(default=timezone.now)
    details = models.CharField(max_length=50, blank=True, null=True)
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    unit = models.ForeignKey(Unit)

    def __str__(self):
        if not self.details:
            return '{0} {1} {2}'.format(self.resource.name, self.amount, self.unit.name)
        else:
            return '{0}:{1} {2} {3}'.format(self.resource.name, self.details, self.amount, self.unit.name)


    @staticmethod
    def get_harvests_by_date(date):
        return get_objects_with_datetime_property_on_given_date(Harvest, date)





class Watering(BaseUserActivityModel):
    watering_id = models.AutoField(primary_key=True)
    project = models.ForeignKey(Project, blank=True, null=True)
    datetime = models.DateTimeField(default=timezone.now)
    target = models.CharField(max_length=50)

    def __str__(self):
        return '{0} - {1} '.format(get_local_time_formatted(self.datetime), self.target)



"""

Observation and Reports

"""

PLANT_PRODUCTIVITY_LEVELS = (
    ('0', 'None'),
    ('1', 'Very-Low'),
    ('2', 'Low'),
    ('3', 'Medium'),
    ('4', 'High'),
    ('5', 'Excessive'),
)


class PlantProductivityReport(BaseUserActivityModel, SpeciesOrCultivarMixin):
    """
    The amount of productivity exhibited by a particular species or cultivar.
    """
    plant_productivity_report_id = models.AutoField(primary_key=True)
    datetime = models.DateTimeField(default=timezone.now)
    species = models.ForeignKey(Species, blank=True, null=True)
    cultivar = models.ForeignKey(Cultivar, blank=True, null=True)
    productivity = models.CharField(max_length=1, choices=PLANT_PRODUCTIVITY_LEVELS)


class Bloom(BaseUserActivityModel, SpeciesOrCultivarMixin):
    bloom_id = models.AutoField(primary_key=True)
    start = models.DateTimeField(default=timezone.now)
    end = models.DateTimeField(blank=True, null=True)
    species = models.ForeignKey(Species, blank=True, null=True)
    cultivar = models.ForeignKey(Cultivar, blank=True, null=True)

    def __str__(self):
        return '{0} - {1}'.format(get_local_time_formatted(self.start), self.get_name())
