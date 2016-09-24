from django.utils import timezone
from django.db import models
from core.managers import NameAscendingOrderManager
from core.models import BaseUserActivityOnSiteModel, BaseModel
from taxonomy.models import LifeForm, Kingdom

AFFINITY_STATES = (
    ('pos', 'Positive'),
    ('neu', 'Neutral'),
    ('neg', 'Negative'),
)

DEFAULT_TYPES = (
    'Born',
    'Death',
    'Disease Present',
    'Healthy',
    'Health Diminishing',
    'Health Improving',
    'Taste Test',
    'Other',
)

DEFAULT_PLANT_OBSERVATION_TYPES = (
    'Bloom Start',
    'Bloom End',
    'Fruit Forming',
    'Fruit Under-Ripe',
    'Fruit Ripe',
    'Fruit Over-Ripe',
    'Fruiting Period Over',
    'Going Dormant',
    'Leafing Out',
    'Germinated',
    'Growth, New',
    'Pest Pressure',
    'Pollination, Sufficient',
    'Pollination, InSufficient',
)


class ObservationType(BaseModel):
    observation_type_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    kingdom_specific = models.ForeignKey(Kingdom, blank=True, null=True)
    objects = NameAscendingOrderManager()

    def __str__(self):
        if self.kingdom_specific:
            return '{0} [{1}]'.format(self.name, self.kingdom_specific.name)
        return self.name


class Observation(BaseUserActivityOnSiteModel):
    observation_id = models.AutoField(primary_key=True)
    observation_type = models.ForeignKey(ObservationType)
    datetime = models.DateTimeField(default=timezone.now)
    life_form = models.ForeignKey(LifeForm, blank=True, null=True)
    affinity = models.CharField(max_length=3, default='neu', choices=AFFINITY_STATES)
    summary = models.CharField(max_length=100, blank=True, null=True)
    observation = models.TextField()


class Prediction(BaseUserActivityOnSiteModel):
    prediction_id = models.AutoField(primary_key=True)
    observation = models.ForeignKey(Observation, blank=True, null=True)
    datetime = models.DateTimeField()
    life_form = models.ForeignKey(LifeForm, blank=True, null=True)
    affinity = models.CharField(max_length=3, default='neu', choices=AFFINITY_STATES)
    summary = models.CharField(max_length=100, blank=True, null=True)
    details = models.TextField()
