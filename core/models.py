import abc
from django.db import models
from django.contrib.auth.models import User


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
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    name = models.CharField(max_length=50)
    description = models.TextField()

