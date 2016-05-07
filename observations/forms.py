from django.forms.models import ModelForm
from observations.models import WeatherReading, Observation
from datetimewidget.widgets import DateTimeWidget


class WeatherReadingForm(ModelForm):
    class Meta:
        model = WeatherReading
        fields = ['datetime', 'state', 'temperature', 'unit']
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
