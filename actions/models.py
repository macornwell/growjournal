from django.db import models
from core.models import BaseUserActivityModel, Project


class Action(BaseUserActivityModel):
    action_id = models.AutoField(primary_key=True)
    project = models.ForeignKey(Project, blank=True, null=True)
    datetime = models.DateTimeField()
    summary = models.CharField(max_length=50, blank=True, null=True)
    action = models.TextField()
