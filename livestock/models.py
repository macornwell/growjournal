from django.db import models
from core.models import BaseUserActivityModel, BaseModel, get_objects_with_datetime_property_on_given_date
from core.utils import get_local_time_formatted
from django.utils import timezone
from observations.models import AFFINITY_STATES


class EggCollection(BaseUserActivityModel):
    egg_collection_id = models.AutoField(primary_key=True)
    datetime = models.DateTimeField(default=timezone.now)
    amount = models.IntegerField()

    @staticmethod
    def get_total_eggs_collected_on_date(date):
        collections = get_objects_with_datetime_property_on_given_date(EggCollection, date)
        amount = 0
        for c in collections:
            amount += c.amount
        return amount

    def __str__(self):
        return '{0} - {1} eggs'.format(get_local_time_formatted(self.datetime), self.amount)


class AnimalReport(BaseUserActivityModel):
    animal_report_id = models.AutoField(primary_key=True)
    datetime = models.DateTimeField(default=timezone.now)
    affinity = models.CharField(max_length=3, default='neu', choices=AFFINITY_STATES)
    summary = models.CharField(max_length=50, blank=True, null=True)
    report_details = models.TextField()