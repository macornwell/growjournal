from django_wizard_form.form_controls import TextBoxControl, NumberInputControl
from django_wizard_form.forms import WizardForm, WizardStep

from core.form_controls import ProjectSelectionControl
from purchase.models import Store, PurchaseEvent
from taxonomy.forms import LifeFormControl


class StoreForm(WizardForm):
    model = Store
    form_title = 'Store'

    def __init__(self):
        self.steps = (
            WizardStep(legend='', form_controls=[
                TextBoxControl(label='Name of Store', name='name'),
                TextBoxControl(label='Url', name='url'),
                ]),
        )

    def apply_instance(self, model):
        self.steps[0].form_controls[0].value = model.name
        self.steps[0].form_controls[1].value = model.url


class PurchaseForm(WizardForm):
    model = PurchaseEvent
    form_title = 'Add Purchase History'

    def __init__(self):
        self.steps = (
            WizardStep(legend='', form_controls=[
                ProjectSelectionControl(label="Select Project (optional)", name='project'),
                LifeFormControl(label="Select a LifeForm (optional)", name='life-form'),
            ]),
            WizardStep(legend='', form_controls=[
                #StoreControl
                #DatetimeControl
            ]),
            WizardStep(legend='', form_controls=[
                NumberInputControl(label='Price', name='price'),
                NumberInputControl(label='Count', name='count', int_only=True),
                #UnitControl
            ]),
        )

    def fill_projects(self, site):
        for step in self.steps:
            for control in step.form_controls:
                if isinstance(control, ProjectSelectionControl):
                    control.fill_projects(site)

    def apply_instance(self, model):
        pass
        #self.steps[0].form_controls[0].value = model.name
