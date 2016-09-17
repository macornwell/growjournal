from django.contrib import admin
from observations.models import Observation, ObservationType, Prediction

admin.site.register(Observation)
admin.site.register(ObservationType)
admin.site.register(Prediction)
