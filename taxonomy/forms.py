from core.forms import TextBoxControl, CheckboxControl, WizardForm, WizardStep, SimpleSelectionControl, WizardControl, NumberInputControl
from taxonomy.models import Kingdom, Genus, Species, Variety, LifeForm, SiteInventory


class KingdomGenusSpeciesControl(WizardControl):
    template_path = 'taxonomy/wizard/kingdom-genus-species-control.html'
    kingdomList = None
    genusList = None
    speciesList = None

    def get_kingdom_list(self):
        if callable(self.kingdomList):
            return self.kingdomList()
        else:
            return self.kingdomList or []

    def get_genus_list(self):
        if callable(self.genusList):
            return self.genusList()
        else:
            return self.genusList or []

    def get_species_list(self):
        if callable(self.speciesList):
            return self.speciesList()
        else:
            return self.speciesList or []


class LifeFormControl(WizardControl):
    template_path = 'taxonomy/wizard/life-form-control.html'



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
                LifeFormControl(),
                NumberInputControl(label='Count', name='count', min=1, max=99999),
            ]),
        )

