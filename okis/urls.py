from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'okis.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^useradmin/$', include('useradmin.urls')),
    url(r'^', include('core.urls')),
    url('^', include('usersite.urls')),
    #url(r'^admin/', include(admin.site.urls)),
    #url(r"^account/", include("account.urls")),
)

urlpatterns += staticfiles_urlpatterns()
