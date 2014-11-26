from django.db import models
from django import forms
from django.forms import ModelForm

from core.models import OkisTemplate

class ChooseDomainForm(ModelForm):
    class Meta:
        model = OkisTemplate
        #fields = [ 'question', 'details', 'tags', 'author', ]


