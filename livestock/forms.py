from django.forms import ModelForm
from datetimewidget.widgets import DateTimeWidget
from livestock.models import EggCollection, AnimalReport


class EggCollectionForm(ModelForm):
    class Meta:
        model = EggCollection
        fields = ['datetime', 'amount']
        widgets = {
            'datetime': DateTimeWidget(attrs={'id': "id-datetime"}, usel10n=True, bootstrap_version=3)
        }


class AnimalReportForm(ModelForm):
    class Meta:
        model = AnimalReport
        fields = ['datetime', 'affinity', 'summary', 'report_details']
        widgets = {
            'datetime': DateTimeWidget(attrs={'id': "id-datetime"}, usel10n=True, bootstrap_version=3 )
        }
