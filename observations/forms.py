from django.forms.models import ModelForm
from observations.models import TemperatureReading, WeatherReading, Observation
from datetimewidget.widgets import DateTimeWidget


class TemperatureReadingForm(ModelForm):
    class Meta:
        model = TemperatureReading
        fields = ['datetime', 'value', 'unit']
        widgets = {
            'datetime': DateTimeWidget(attrs={'id': "id-datetime"}, usel10n=True, bootstrap_version=3 )
        }


class WeatherReadingForm(ModelForm):
    class Meta:
        model = WeatherReading
        fields = ['datetime', 'state']
        widgets = {
            'datetime': DateTimeWidget(attrs={'id': "id-datetime"}, usel10n=True, bootstrap_version=3)
        }


class ObservationForm(ModelForm):
    class Meta:
        model = Observation
        fields = ['project', 'observation_date', 'summary', 'observation']
        widgets = {
            'observation_date': DateTimeWidget(attrs={'id': "id-observation_date"}, usel10n=True, bootstrap_version=3)
        }
