from django.forms import ModelForm
from core.models import WebsiteFeedback
from datetimewidget.widgets import DateTimeWidget


class FeedbackForm(ModelForm):
    class Meta:
        model = WebsiteFeedback
        fields = ['datetime', 'feedback']
        widgets = {
            'datetime': DateTimeWidget(attrs={'id': "id-datetime"}, usel10n=True, bootstrap_version=3 )
        }



