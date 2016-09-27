from django.utils import timezone
from django.db import models
from core.models import BaseUserActivityOnSiteModel, Project
from taxonomy.models import LifeForm
from geography.models import Location


class DeployEvent(BaseUserActivityOnSiteModel):
    planting_record = models.AutoField(primary_key=True)
    life_form = models.ForeignKey(LifeForm)
    project = models.ForeignKey(Project, blank=True, null=True)
    datetime = models.DateTimeField(default=timezone.now)
    location = models.TextField(blank=True, null=True)
    location_detail = models.ForeignKey(Location, blank=True, null=True)
    count = models.PositiveIntegerField(blank=True, null=True)

