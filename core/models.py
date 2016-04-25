import abc
from django.db import models
from django.contrib.auth.models import User


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
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

