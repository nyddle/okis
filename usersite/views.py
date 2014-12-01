from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.views.generic import View


class UserSiteView(View):

    def get(self, request):
        return HttpResponse('usersite')

