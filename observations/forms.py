from django.forms.models import ModelForm
from observations.models import TemperatureReading

class TemperatureReadingForm(ModelForm):
    class Meta:
        model = TemperatureReading
        fields = ['value', 'unit']
