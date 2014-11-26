from django.db import models
from django import forms
from django.forms import Form

from core.models import OkisTemplate, OkisSite

class ChooseDomainForm(Form):
    domain = forms.CharField(label='Your domain', max_length=100)

    def clean_domain(self):
        domain = self.cleaned_data['domain']
        if OkisSite.objects.filter(name=domain).exists():
            raise ValidationError("Domain already exists")

        # Always return the cleaned data, whether you have changed it or
        # not.
        return domain
