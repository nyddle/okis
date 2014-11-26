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
    email = forms.EmailField(label='Your email', max_length=100)
    confirm_email = forms.EmailField(label='Confirm email', max_length=100)

    def clean_email(self):

        if 'email' in self.cleaned_data:
            email = self.cleaned_data['email']
            #TODO: check if email exists
            """
            if OkisSite.objects.filter(name=domain).exists():
                raise ValidationError("Domain already exists")
            """
            return email
        else:
            raise ValidationError("Invalid email address.")

    def clean(self):
        form_data = self.cleaned_data

        if ('email' not in form_data) or ('confirm_email' not in form_data):
            raise ValidationError("Invalid email address.")

        if form_data['email'] != form_data['confirm_email']:
            self._errors["email"] = ["Emails do not match"] # Will raise a error message
            del form_data['confirm_email']
        return form_data

