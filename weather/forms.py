from django.forms.models import ModelForm
from weather.models import WeatherReading
from datetimewidget.widgets import DateTimeWidget


class WeatherReadingForm(ModelForm):
    class Meta:
        model = WeatherReading
        fields = ['datetime', 'state', 'temperature', 'unit']
        widgets = {
            'datetime': DateTimeWidget(attrs={'id': "id-datetime"}, usel10n=True, bootstrap_version=3)
        }

