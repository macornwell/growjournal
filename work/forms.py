from django.forms import Select
from django.forms.models import ModelForm
from datetimewidget.widgets import DateTimeWidget
from work.models import WorkCompleted

class WorkCompletedForm(ModelForm):
    class Meta:
        model = WorkCompleted
        fields = ['project', 'datetime', 'summary', 'work']
        widgets = {
            'datetime': DateTimeWidget(attrs={'id': "id-datetime"}, usel10n=True, bootstrap_version=3)
        }
