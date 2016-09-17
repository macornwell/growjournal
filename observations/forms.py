from django.forms.models import ModelForm
from django import forms
from core.models import Project
from observations.models import Observation
from datetimewidget.widgets import DateTimeWidget



class ObservationForm(ModelForm):
    project = forms.ModelChoiceField(queryset=Project.objects.order_by('name'))

    class Meta:
        model = Observation
        fields = ['project', 'datetime', 'affinity', 'summary', 'observation']
        widgets = {
            'observation_date': DateTimeWidget(attrs={'id': "id-observation_date"}, usel10n=True, bootstrap_version=3)
        }
