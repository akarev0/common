from django.forms import ModelForm

from mycore.models import Journal


class JournalForm(ModelForm):
    class Meta:
        model = Journal
        fields = ('key_out_date', 'tenant', 'key')
