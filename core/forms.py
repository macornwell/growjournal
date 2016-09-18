from django.forms import ModelForm
from core.models import WebsiteFeedback, Site
from django.utils.html import escape, format_html
from django.utils.safestring import mark_safe
from datetimewidget.widgets import DateTimeWidget


class WizardForm:
    model_type = None
    model = None
    steps = []


class WizardStep:
    legend = None
    form_controls = []
    scripts = []

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)


class WizardControl:
    template_path = None
    template = None

    def generate_template(self):
        raise NotImplemented()


class SimpleControl(WizardControl):
    label = None
    name = None
    id = None
    classes = []

    def get_kargs(self):
        return {
            'id': self.id,
            'label': self.label,
            'name': self.name,
            'classes': self.classes,
        }

    def generate_template(self):
        kwargs = self.get_kargs()
        snippet = format_html(self.template, kwargs)
        return mark_safe(snippet)

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)


class CheckboxControl(SimpleControl):
    value = 'checked'
    is_checked = False
    template = """
    <label>{{ label }}</label>
    <input type="checkbox"
        {% if id %}
            id="{{ id }}"
        {% endif %}
        name="{{ name }}"
        value="{{ value }}"
        class="form-control
        {% for className in classes %}
        {% endfor %}
        "
        {% if is_checked %}
            checked
        {% endif %}
        >
    """


class TextBoxControl(SimpleControl):
    template = """
    <label>{{ label }}</label>
    <input class="form-control" type="text" name="{{ name }}">
    """



class SiteForm(WizardForm):
    model = Site
    model_type = 'Site'
    steps = (
            WizardStep(legend='Add New', form_controls=[
                TextBoxControl(label='Name', name='name'),
                CheckboxControl(label='Is Publicly Viewable?', name='public-viewable', is_checked=True),
                CheckboxControl(label='Is Publicly Joinable?', name='public-joinable'),
            ]),
    )



class FeedbackForm(ModelForm):
    class Meta:
        model = WebsiteFeedback
        fields = ['datetime', 'feedback']
        widgets = {
            'datetime': DateTimeWidget(attrs={'id': "id-datetime"}, usel10n=True, bootstrap_version=3 )
        }



