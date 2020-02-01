from django import forms

from mycore.models import Key, Tenant, Journal


class JournalForm(forms.Form):
    tenant_name = forms.CharField()
    key_id = forms.NumberInput()

    def save_key_transfer(self):
        key = Key.objects.get(room_id=int(self.data['key_id']))
        tenant = Tenant.objects.get(first_name=self.data['tenant_name'])
        transfer = Journal(key_id=key, tenant_id=tenant)
        transfer.save()
