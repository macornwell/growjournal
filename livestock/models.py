from django.db import models
from core.models import BaseUserActivityModel, BaseModel


class EggCollection(BaseUserActivityModel):
    egg_collection_id = models.AutoField(primary_key=True)
    datetime = models.DateTimeField()
    amount = models.IntegerField(max_length=4)

class Animal(BaseModel):
    name = models.CharField(max_length=50)

class AnimalMovement(BaseUserActivityModel):
    animal = models.ForeignKey(Animal)
    datetime = models.DateTimeField()
    fromArea = models.CharField(max_length=50)
    toArea = models.CharField(max_length=50)

