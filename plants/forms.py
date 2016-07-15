from django.contrib import messages
from django import forms
from django.forms.models import ModelForm
from core.models import Project
from plants.models import Harvest, Bloom, PlantProductivityReport, Watering, Resource, PlantReport, Species, Cultivar, Genus
from datetimewidget.widgets import DateTimeWidget


class HarvestForm(ModelForm):
    resource = forms.ModelChoiceField(queryset=Resource.objects.order_by('name'))

    class Meta:
        model = Harvest
        fields = ['resource', 'datetime', 'details', 'amount', 'unit', 'notes']
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
    species = forms.ModelChoiceField(queryset=Species.objects.order_by('latin_name'), required=False)
    cultivar = forms.ModelChoiceField(queryset=Cultivar.objects.order_by('name'), required=False)

    class Meta:
        model = PlantProductivityReport
        fields = ['species', 'cultivar', 'datetime', 'productivity', 'notes']
        widgets = {
            'datetime': DateTimeWidget(attrs={'id': "id-datetime"}, usel10n=True, bootstrap_version=3 )
        }


class WateringForm(ModelForm):
    project = forms.ModelChoiceField(queryset=Project.objects.order_by('name'))

    class Meta:
        model = Watering
        fields = ['project', 'datetime', 'target']
        widgets = {
            'datetime': DateTimeWidget(attrs={'id': "id-datetime"}, usel10n=True, bootstrap_version=3 )
        }


class ResourceForm(ModelForm):
    species = forms.ModelChoiceField(queryset=Species.objects.order_by('latin_name'), required=False)
    cultivar = forms.ModelChoiceField(queryset=Cultivar.objects.order_by('name'), required=False)

    class Meta:
        model = Resource
        fields = ['name', 'species', 'cultivar', 'description']


class PlantReportForm(ModelForm):
    species = forms.ModelChoiceField(queryset=Species.objects.order_by('latin_name'), required=False)
    cultivar = forms.ModelChoiceField(queryset=Cultivar.objects.order_by('name'), required=False)


    class Meta:
        model = PlantReport
        fields = ['datetime', 'species', 'cultivar', 'affinity', 'summary', 'report_details']
        widgets = {
            'datetime': DateTimeWidget(attrs={'id': "id-datetime"}, usel10n=True, bootstrap_version=3 )
        }


def cultivar_species_validator(request, form):
    cultivar = form.cleaned_data['cultivar']
    species = form.cleaned_data['species']
    if cultivar and species:
        if cultivar.species != species:
            messages.error(request, 'Cultivar and species cannot be different')
            return False
    return True
