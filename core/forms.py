from core.models import Site, Unit, Project
from django.utils import timezone
from django.utils.html import escape, format_html
from django.utils.safestring import mark_safe
from datetimewidget.widgets import DateTimeWidget


"""
Controls
"""

class WizardControl:
    template_path = None
    template = None
    label = ''
    name = ''
    id = ''
    classes = []
    value = None

    def generate_context(self):
        return {
            'id': self.id,
            'label': self.label,
            'name': self.name,
            'classes': self.classes,
        }

    def generate_template(self):
        kwargs = self.generate_context()
        snippet = format_html(self.template, kwargs)
        return mark_safe(snippet)

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)


class NumberInputControl(WizardControl):
    template_path = 'wizard/number-input-control.html'
    int_only = False
    min = -1
    max = -1


class SimpleSelectionControl(WizardControl):
    selections = ()
    selected_value = None
    template_path = 'wizard/selection.html'

    def get_selections(self):
        """
        get_selections
        Format is a tuple of the 'value' and 'name' for an <option value='value'>name</option>
        """
        return self.selections

    def get_selected_value(self):
        return self.selected_value

    def generate_context(self):
        z = super(SimpleSelectionControl, self).generate_context().copy()
        z['selected_value'] = self.get_selected_value()
        return z


class CheckboxControl(WizardControl):
    value = 'checked'
    is_checked = False
    template_path = 'wizard/checkbox.html'


class TextBoxControl(WizardControl):
    template_path = 'wizard/textbox.html'


class TextAreaControl(WizardControl):
    template_path = 'wizard/textarea.html'


class DateTimeControl(WizardControl):
    id = 'datetime'
    name = 'datetime'
    use_now = False

    def generate_template(self):
        currentValue = None
        if self.use_now:
            currentValue = timezone.now()
        template = ''
        if self.label:
            template += "<label>{0}</label>".format(self.label)
        template += DateTimeWidget(attrs={'id': self.id}, usel10n=True, bootstrap_version=3).render(self.name, currentValue)
        return mark_safe(template)


class ProjectSelectionControl(SimpleSelectionControl):

    def fill_projects(self, site):
        projects = Project.objects.get_projects_for_site(site)
        list = [(-1, '---')]
        for p in projects:
            list.append((p.project_id, p.name))
        list = sorted(list, key=lambda x: x[1])
        self.selections = tuple(list)


class HiddenSiteControl(WizardControl):
    template_path = 'core/wizard/hidden-site.html'


"""
Forms
"""

class WizardForm:
    form_title = None
    model = None
    steps = []

    def apply_instance(self, instance):
        raise NotImplemented()


class WizardStep:
    name = ''
    legend = ''
    form_controls = []
    scripts = []

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

"""
Instances

"""

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
