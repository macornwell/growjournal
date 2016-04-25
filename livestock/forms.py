from django.forms import ModelForm
from datetimewidget.widgets import DateTimeWidget
from livestock.models import EggCollection

class EggCollectionForm(ModelForm):
    class Meta:
        model = EggCollection
        fields = ['datetime', 'amount']
        widgets = {
            'datetime': DateTimeWidget(attrs={'id': "id-datetime"}, usel10n=True, bootstrap_version=3)
        }
