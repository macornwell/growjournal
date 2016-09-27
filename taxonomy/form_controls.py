from django_wizard_form.form_controls import WizardControl

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