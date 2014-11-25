from django.shortcuts import render

from django.shortcuts import render, redirect, HttpResponse, get_object_or_404

from django.http import Http404
from django.http import HttpResponseNotFound

from django.views.generic import View
from django.views.generic import ListView
from django.views.generic.edit import FormView, ProcessFormView, CreateView

from .models import OkisTemplate, OKIS_THEMES


class ThemesView(View):

    def get(self, request):
        return render(request, 'reg.html', {'themes': OKIS_THEMES })


