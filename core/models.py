from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


def get_objects_with_datetime_property_on_given_date(modelClass, date):
    return modelClass.objects.filter(datetime__year=date.year,
                                     datetime__month=date.month,
                                     datetime__day=date.day)


class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class BaseUserActivityModel(BaseModel):
    user = models.ForeignKey(User)

    class Meta:
        abstract = True


class Project(models.Model):
    project_id = models.AutoField(primary_key=True)
    completed = models.BooleanField(default=False)
    start_date = models.DateField(default=timezone.now, blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Unit(BaseModel):
    """
    A unit of measurement.
    """
    unit_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name


class Note(BaseUserActivityModel):
    notes_id = models.AutoField(primary_key=True)
    notes = models.TextField()
    datetime = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.notes