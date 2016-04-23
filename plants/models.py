from django.db import models
from core.models import BaseModel, BaseUserActivityModel, Project

# Create your models here.

class Plant(BaseModel):
    plant_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    pass


class Bloom(BaseUserActivityModel):
    bloom_id = models.AutoField()
    start = models.DateTimeField()
    end = models.DateTimeField(blank=True, null=True)
    plant = models.ForeignKey(Plant)


class Unit(BaseModel):
    unit_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, unique=True)


class HarvestSource(BaseModel):
    harvest_source_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)


class Harvest(BaseUserActivityModel):
    harvest_id = models.AutoField(primary_key=True)
    project = models.ForeignKey(Project, blank=True, null=True)
    plant = models.ForeignKey(Plant)
    harvest_date = models.DateTimeField()
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    unit = models.ForeignKey(Unit)


class Watering(BaseUserActivityModel):
    watering_id = models.AutoField(primary_key=True)
    datetime = models.DateTimeField()
    plant = models.ForeignKey(Plant)
