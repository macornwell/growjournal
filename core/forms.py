from django_wizard_form.forms import WizardForm, WizardStep
from django_wizard_form.form_controls import TextBoxControl, CheckboxControl, TextAreaControl, DateTimeControl
from core.models import Site, Unit, Project
from core.form_controls import HiddenSiteControl


class UnitForm(WizardForm):
    model = Unit
    form_title = 'Unit'

    def __init__(self):
        self.steps = (
            WizardStep(legend='', form_controls=[
                TextBoxControl(label='Name of Unit', name='name'),
                ]),
        )

    def apply_instance(self, unit):
        self.steps[0].form_controls[0].value = unit.name


class SiteForm(WizardForm):
    model = Site
    form_title = 'Site'

    def __init__(self):
        self.steps = (
            WizardStep(legend='', form_controls=[
                TextBoxControl(label='Name', name='name'),
                CheckboxControl(label='Is Publicly Viewable?', name='public-viewable', is_checked=True),
                CheckboxControl(label='Is Publicly Joinable?', name='public-joinable'),
            ]),
        )

    def apply_instance(self, site):
        self.steps[0].form_controls[0].value = site.name
        self.steps[0].form_controls[1].is_checked = site.is_public_viewable
        self.steps[0].form_controls[2].is_checked = site.is_public_joinable


class ProjectForm(WizardForm):
    model = Project
    form_title = 'Project'

    def __init__(self):
        self.steps = (
            WizardStep(legend='Basic Info', form_controls=[
                HiddenSiteControl(),
                TextBoxControl(label='Name', name='name'),
                TextAreaControl(label='Description', name='description'),
            ]),
            WizardStep(legend='Dates', form_controls=[
                DateTimeControl(label='Date Started', name='date-started', id='date-started', use_now=True),
                DateTimeControl(label='Date Ended', name='date-ended', id='date-ended'),
            ]),
            WizardStep(legend='Permissions', form_controls=[
                CheckboxControl(label='Is Perpetual', name='is-perpetual'),
                CheckboxControl(label='Is Viewable To Public', name='is-public-viewable'),
            ]),
        )

    def apply_instance(self, site):
        pass
        #self.steps[0].form_controls[0].value = site.name
