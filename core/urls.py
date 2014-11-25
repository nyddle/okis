from django.conf.urls import patterns, include, url
from django.shortcuts import render_to_response

from django.views.generic.base import TemplateView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'okis.views.home', name='home'),
    url(r'^reg/$', TemplateView.as_view(template_name='reg.html'), name='reg'),
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
)
