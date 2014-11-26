from django.db import models
from django import forms
from django.forms import Form
from django.core.exceptions import ValidationError

from core.models import OkisTemplate, OkisSite

class ChooseDomainForm(Form):
    domain = forms.CharField(label='Your domain', max_length=100)

    def clean_domain(self):
        domain = self.cleaned_data['domain']
        if OkisSite.objects.filter(name=domain).exists():
            raise ValidationError("Domain already exists")

        return domain
