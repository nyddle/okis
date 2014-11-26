from django.shortcuts import render

from django.http import Http404

from django.views.generic import View, ListView
from django.views.generic.edit import FormView, ProcessFormView, CreateView

from .models import OkisTemplate, OKIS_THEMES
from .forms import ChooseDomainForm, ChooseEmailForm

from django.template.defaulttags import register

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)


class ThemesView(View):

    def get(self, request):
        return render(request, 'choose_theme.html', {'themes': OKIS_THEMES, 'table' : [ ['auto', 'business', 'computers'], ['sport',] ] })

class OkisTemplateListView(ListView):
    model = OkisTemplate
    template_name = 'choose_template.html'

    def get(self, request, theme):
        try:
            templates = OkisTemplate.objects.filter(theme=theme)
        except OkisTemplate.DoesNotExist:
            raise Http404
        return render(request, 'choose_template.html', { 'templates' : templates })

class ChooseDomainView(FormView):
    template_name = 'choose_domain.html'
    form_class = ChooseDomainForm
    success_url = '/register'

    def form_valid(self, form):
        return super(ChooseDomainView, self).form_valid(form)

class ChooseEmailView(FormView):
    template_name = 'choose_email.html'
    form_class = ChooseEmailForm
    success_url = '/register'

    def form_valid(self, form):
        return super(ChooseEmailView, self).form_valid(form)




