from django.utils import timezone
from django.db import models
from core.models import BaseModel, BaseUserActivityOnSiteModel, Project, Unit
from taxonomy.models import LifeForm
from geography.models import Location
from djmoney.models.fields import MoneyField


class Store(BaseModel):
    store_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, unique=True)
    url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name


class PurchaseEvent(BaseUserActivityOnSiteModel):
    purchase_record_id = models.AutoField(primary_key=True)
    life_form = models.ForeignKey(LifeForm)
    project = models.ForeignKey(Project, blank=True, null=True)
    datetime = models.DateTimeField(default=timezone.now)
    store = models.ForeignKey(Store, blank=True, null=True)
    count = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    unit = models.ForeignKey(Unit, blank=True, null=True)
    price = MoneyField(default_currency='USD', max_digits=10, decimal_places=2, blank=True, null=True)



