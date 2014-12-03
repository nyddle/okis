from django.conf.urls import patterns, include, url
from django.shortcuts import render_to_response

from django.views.generic.base import TemplateView

from .views import UserAdminView


urlpatterns = patterns('',
    #url(r'^', UserAdminView.as_view(), name='useradmin'),
    url(r'^menu', TemplateView.as_view(template_name='useradmin/menu.html'), name='menu'),
    url(r'^pages', TemplateView.as_view(template_name='useradmin/pages.html'), name='pages'),
    url(r'^photo', TemplateView.as_view(template_name='useradmin/photo.html'), name='photo'),
    url(r'^', TemplateView.as_view(template_name='useradmin/index.html'), name='useradmin.index'),
)

