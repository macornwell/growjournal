from django.forms import ModelForm
from core.models import WebsiteFeedback, Site
from django.utils.html import escape, format_html
from django.utils.safestring import mark_safe
from datetimewidget.widgets import DateTimeWidget


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


class WizardControl:
    template_path = None
    template = None
    label = ''
    name = ''
    id = ''
    classes = []

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
    min = -1
    max = -1



class SimpleSelectionControl(WizardControl):
    """
    selections
    Format is a tuple of the 'value' and 'name' for an <option value='value'>name</option>
    """
    selections = ()
    selected_value = None
    template_path = 'wizard/selection.html'

    def generate_context(self):
        z = super(SimpleSelectionControl, self).generate_context().copy()
        z['selected_value'] = self.selected_value
        return z

class CheckboxControl(WizardControl):
    value = 'checked'
    is_checked = False
    template_path = 'wizard/checkbox.html'


class TextBoxControl(WizardControl):
    template_path = 'wizard/textbox.html'


class SiteForm(WizardForm):
    model = Site
    model_type = 'Site'
    steps = ()

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



class FeedbackForm(ModelForm):
    class Meta:
        model = WebsiteFeedback
        fields = ['datetime', 'feedback']
        widgets = {
            'datetime': DateTimeWidget(attrs={'id': "id-datetime"}, usel10n=True, bootstrap_version=3 )
        }



