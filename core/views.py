from django.shortcuts import render

from django.http import Http404

from django.views.generic import View, ListView
from django.views.generic.edit import FormView, ProcessFormView, CreateView

from .models import OkisTemplate, OKIS_THEMES, OkisSite
from .forms import ChooseDomainForm, ChooseEmailForm, MySignupForm

from django.template.defaulttags import register

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)


import account.forms
import account.views


class LoginView(account.views.LoginView):

    form_class = account.forms.LoginEmailForm

class SignupView(account.views.SignupView):

    form_class = MySignupForm

    def generate_username(self, form):
        # do something to generate a unique username (required by the
        # Django User model, unfortunately)
        username = form.fields['email']
        return username

    def after_signup(self, form):
        theme = self.request.session.get('theme')
        template = self.request.session.get('template')
        template_id = self.request.session.get('template_id')
        domain = self.request.session.get('domain')

        okis_template = OkisTemplate.objects.get(pk=template_id)
        #okis_site = OkisSite.objects.create(owner=self.request.user, template=okis_template, name=domain)
        okis_site = OkisSite.objects.create(owner_email=form.fields['email'], template=okis_template, name=domain)
        okis_site.save()
        super().after_signup(form)


class ThemesView(View):

    def get(self, request):
        return render(request, 'core/choose_theme.html', {'themes': OKIS_THEMES, 'table' : [ ['auto', 'business', 'computers'], ['sport',] ] })

class OkisTemplateListView(ListView):
    model = OkisTemplate

    def get(self, request, theme):
        try:
            templates = OkisTemplate.objects.filter(theme=theme)
            request.session['theme'] = theme
        except OkisTemplate.DoesNotExist:
            raise Http404
        return render(request, 'core/choose_template.html', { 'templates' : templates })

class ChooseDomainView(FormView):
    template_name = 'core/choose_domain.html'
    form_class = ChooseDomainForm
    success_url = '/account/signup/'

    def get(self, request):
        request.session['theme'] = request.GET['theme']
        request.session['template'] = request.GET['template']
        request.session['template_id'] = request.GET['template_id']
        return super().get(request)

    def post(self, request):
        request.session['domain'] = request.POST['domain']
        return super().post(request)

