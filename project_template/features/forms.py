from django import forms

from .models import *


class NewFeatureRequestForm(forms.ModelForm):
    class Meta:
        model = FeatureRequest
        fields = ('title', 'description', 'client', 'target_date',
            'ticket_url', 'product_area')

    def save(self, created_by):
        instance = super(NewFeatureRequestForm, self).save(commit=False)
        instance.created_by = created_by
        instance.save()
        return instance