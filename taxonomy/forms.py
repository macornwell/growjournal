from django_wizard_form.forms import WizardForm, WizardStep
from django_wizard_form.form_controls import SimpleSelectionControl, TextBoxControl, NumberInputControl
from core.form_controls import HiddenSiteControl
from taxonomy.form_controls import KingdomGenusSpeciesControl, LifeFormControl
from taxonomy.models import Kingdom, Genus, Species, Variety, SiteInventory


class GenusForm(WizardForm):
    model = Genus
    form_title = 'Add New Genus'

    def __init__(self):
        self.steps = (
            WizardStep(legend='', form_controls=[
                SimpleSelectionControl(label='Kingdoms', name='kingdom', selections=self.get_selections()),
                TextBoxControl(label='Name', name='name'),
                TextBoxControl(label='Latin Name', name='latin-name'),
            ]),
        )

    def get_selections(self):
        kingdoms = [(obj.name, obj.name) for obj in Kingdom.objects.all()]
        return kingdoms

    def apply_instance(self, genus):
        self.steps[0].form_controls[0].selected_value = genus.kingdom.name
        self.steps[0].form_controls[1].value = genus.name
        self.steps[0].form_controls[2].value = genus.latin_name


class SpeciesForm(WizardForm):
    model = Species
    form_title = 'Add New Species'

    def __init__(self):
        self.steps = (
            WizardStep(name='Genus', legend='Select Genus', form_controls=[
                KingdomGenusSpeciesControl(genusList=self.get_genusList, kingdomList=self.get_kingdomList),
            ]),
            WizardStep(name='Details', legend='Details', form_controls=[
                TextBoxControl(label='Name', name='name'),
                TextBoxControl(label='Latin Name', name='latin-name'),
            ]),
        )
    def get_genusList(self):
        return Genus.objects.all()

    def get_kingdomList(self):
        return Kingdom.objects.all()



class VarietyForm(WizardForm):
    model = Variety
    form_title = 'Add New Variety'

    def __init__(self):
        self.steps = (
            WizardStep(name='Species', legend='Select Species', form_controls=[
                KingdomGenusSpeciesControl(genusList=self.get_genusList, kingdomList=self.get_kingdomList, speciesList=self.get_speciesList),
            ]),
            WizardStep(name='Details', legend='Details', form_controls=[
                TextBoxControl(label='Name', name='name'),
            ])
        )

    def get_genusList(self):
        return Genus.objects.all()

    def get_kingdomList(self):
        return Kingdom.objects.all()

    def get_speciesList(self):
        return Species.objects.all()


class SiteInventoryForm(WizardForm):
    model = SiteInventory
    form_title = 'Add Life Forms'

    def __init__(self):
        self.steps = (
            WizardStep(form_controls=[
                HiddenSiteControl(),
                LifeFormControl(),
                NumberInputControl(label='Count', name='count', int_only=True, min=1, max=99999),
            ]),
        )

