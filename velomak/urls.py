# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^comments/', include('django.contrib.comments.urls')),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^$', include('blog.urls'))
)
