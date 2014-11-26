from django.db import models
from django import forms
from django.forms import Form
from django.core.exceptions import ValidationError

from core.models import OkisTemplate, OkisSite

class ChooseDomainForm(Form):
    domain = forms.CharField(label='Your domain', max_length=100)

    def clean_domain(self):
        domain = self.cleaned_data['domain']
        #TODO: check domain is valid [a-z][0-9]+
        if OkisSite.objects.filter(name=domain).exists():
            raise ValidationError("Domain already exists")

        return domain

class ChooseEmailForm(Form):
    email = forms.CharField(label='Your email', max_length=100)
    confirm_email = forms.CharField(label='Confirm email', max_length=100)

    def clean_email(self):
        email = self.cleaned_data['email']
        email2 = self.cleaned_data['confirm_email']
        #TODO: check if email exists
        #TODO: check if email is valid
        """
        if OkisSite.objects.filter(name=domain).exists():
            raise ValidationError("Domain already exists")
        """
        return email

