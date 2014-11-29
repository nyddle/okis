from django.shortcuts import render

from django.http import Http404

from django.views.generic import View, ListView
from django.views.generic.edit import FormView, ProcessFormView, CreateView

from .models import OkisTemplate, OKIS_THEMES
from .forms import ChooseDomainForm, ChooseEmailForm
#from .forms import SignupForm as MySignupForm
from .forms import MySignupForm

from django.template.defaulttags import register

from account.models import SignupCode, EmailAddress, EmailConfirmation, Account, AccountDeletion, EmailAddressManager

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)


import account.forms
import account.views


class LoginView(account.views.LoginView):

    form_class = account.forms.LoginEmailForm

class SignupView(account.views.SignupView):

    form_class = MySignupForm

    def get(self, request):
        #AccountDeletion.mark(Account.filter(user='nyddle@gmail.com'))
        emails = EmailAddressManager()
        allemails = emails.all()
        email = EmailAddress.objects.get(email='nyddle@gmail.com')
        #acc = Account.objects.get(email='nyddle@gmail.com')
        print(dir(allemails))
        #EmailAddressManager().get_queryset().filter(email='nyddle@gmail.com')
        return super().get(request)

    def generate_username(self, form):
        # do something to generate a unique username (required by the
        # Django User model, unfortunately)
        username = form.fields['email']
        return username

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
        return super().get(request)

    def post(self, request):
        #TODO: verify domain name
        request.session['domain'] = request.POST['domain']
        return super().post(request)

