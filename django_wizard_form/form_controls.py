from django.utils.html import format_html
from django.utils.safestring import mark_safe
from django.utils import timezone

from datetimewidget.widgets import DateTimeWidget


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
