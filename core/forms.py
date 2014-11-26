from django.db import models
from django import forms
from django.forms import ModelForm

from core.models import OkisTemplate, OkisSite

class ChooseDomainForm(ModelForm):
    class Meta:
        model = OkisSite
        fields = [ 'name', 'owner', ]

