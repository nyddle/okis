from django.shortcuts import render
from django.shortcuts import redirect

from django.http import HttpResponse
from django.http import Http404

from django.views.generic import View

from core.models import OkisSite


class UserSiteView(View):

    def get(self, request, subdomain):
        try:
            usersite = OkisSite.objects.get(name=subdomain)
        except OkisSite.DoesNotExist:
            raise Http404
        return render(request, 'usersite/index.html')


