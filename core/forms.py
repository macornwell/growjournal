from django.forms import ModelForm
from core.models import Note
from datetimewidget.widgets import DateTimeWidget


class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = ['datetime', 'notes']
        widgets = {
            'datetime': DateTimeWidget(attrs={'id': "id-datetime"}, usel10n=True, bootstrap_version=3 )
        }



