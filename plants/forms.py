from django.contrib import messages
from django.forms.models import ModelForm
from plants.models import Harvest, Bloom, PlantProductivityReport, Watering, Resource
from datetimewidget.widgets import DateTimeWidget


class HarvestForm(ModelForm):
    class Meta:
        model = Harvest
        fields = ['resource', 'datetime', 'details', 'amount', 'unit']
        widgets = {
            'datetime': DateTimeWidget(attrs={'id': "id-datetime"}, usel10n=True, bootstrap_version=3 )
        }


class BloomForm(ModelForm):
    class Meta:
        model = Bloom
        fields = ['start', 'end', 'species', 'cultivar']
        widgets = {
            'start': DateTimeWidget(attrs={'id': "id-start-datetime"}, usel10n=True, bootstrap_version=3 ),
            'end': DateTimeWidget(attrs={'id': "id-end-datetime"}, usel10n=True, bootstrap_version=3 )
        }


class PlantProductivityForm(ModelForm):
    class Meta:
        model = PlantProductivityReport
        fields = ['species', 'datetime', 'cultivar', 'productivity']
        widgets = {
            'datetime': DateTimeWidget(attrs={'id': "id-datetime"}, usel10n=True, bootstrap_version=3 )
        }


class WateringForm(ModelForm):
    class Meta:
        model = Watering
        fields = ['project', 'datetime', 'target']
        widgets = {
            'datetime': DateTimeWidget(attrs={'id': "id-datetime"}, usel10n=True, bootstrap_version=3 )
        }


class ResourceForm(ModelForm):
    class Meta:
        model = Resource
        fields = ['name', 'species', 'cultivar', 'description']

def cultivar_species_validator(request, form):
    cultivar = form.cleaned_data['cultivar']
    species = form.cleaned_data['species']
    if cultivar and species:
        if cultivar.species != species:
            messages.error(request, 'Cultivar and species cannot be different')
            return False
    return True
