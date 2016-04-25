from django.utils import timezone
from django.db import models
from core.models import BaseUserActivityModel, Project
from core.utils import get_summary_with_datetime


class WorkCompleted(BaseUserActivityModel):
    work_completed_id = models.AutoField(primary_key=True)
    project = models.ForeignKey(Project, blank=True, null=True)
    datetime = models.DateTimeField(default=timezone.now)
    summary = models.CharField(max_length=50, blank=True, null=True)
    work = models.TextField()

    def __str__(self):
        return get_summary_with_datetime(self.datetime, self.work, self.summary)


