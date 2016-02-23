from django import forms

from .models import *


class NewFeatureRequestForm(forms.ModelForm):
    client_priority = forms.IntegerField()
    class Meta:
        model = FeatureRequest
        fields = ('title', 'description', 'client', 'client_priority',
            'target_date', 'ticket_url', 'product_area')

    def save(self, created_by):
        instance = super(NewFeatureRequestForm, self).save(commit=False)
        instance.created_by = created_by
        instance.save()
        instance.reorder_client_priority(self.cleaned_data['client_priority'])
        return instance

