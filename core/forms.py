from django.forms import ModelForm
from core.models import Feedback
from datetimewidget.widgets import DateTimeWidget


class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        fields = ['datetime', 'feedback']
        widgets = {
            'datetime': DateTimeWidget(attrs={'id': "id-datetime"}, usel10n=True, bootstrap_version=3 )
        }



