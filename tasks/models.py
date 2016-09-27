from django.utils import timezone
from django.db import models
from core.models import BaseUserActivityModel, Project, BaseModel, Unit
from taxonomy.models import LifeForm


class TaskType(BaseModel):
    task_type_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)


class Task(BaseUserActivityModel):
    task_id = models.AutoField(primary_key=True)
    task_type = models.ForeignKey(TaskType)
    project = models.ForeignKey(Project)
    start = models.DateTimeField(default=timezone.now)
    ended = models.DateTimeField(blank=True, null=True)
    summary = models.CharField(max_length=100, blank=True, null=True)
    details = models.TextField()


class TaskOutput(BaseModel):
    task_output_id = models.AutoField(primary_key=True)
    task = models.ForeignKey(Task)
    life_form = models.ForeignKey(LifeForm, blank=True, null=True)
    amount = models.DecimalField(decimal_places=2, max_digits=8)
    unit = models.ForeignKey(Unit)
    details = models.TextField(blank=True, null=True)


