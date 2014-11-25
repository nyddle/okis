from django.conf.urls import patterns, include, url
from django.shortcuts import render_to_response

from django.views.generic.base import TemplateView

from .views import ThemesView, OkisTemplateListView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^choose_theme/$', ThemesView.as_view(), name='choose_theme'),
    url(r'^choose_template/$', OkisTemplateListView.as_view(), name='choose_template'),
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
)
