from django.conf.urls import patterns, include, url
from django.shortcuts import render_to_response

from django.views.generic.base import TemplateView

from .views import ThemesView, OkisTemplateListView, ChooseDomainView, SignupView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^account/signup/$', SignupView.as_view(), name='signup'),
    url(r"^account/", include("account.urls")),
    url(r'^choose_theme/$', ThemesView.as_view(), name='choose_theme'),
    url(r'^choose_template/(?P<theme>\w+)/$', OkisTemplateListView.as_view(), name='choose_template'),
    url(r'^choose_domain/$', ChooseDomainView.as_view(), name='choose_domain'),
    url(r'^$', TemplateView.as_view(template_name='core/home.html'), name='home'),
)

