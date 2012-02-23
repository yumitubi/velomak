# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, include, url
from velomak.blog.views import blog, cur_post, about, cur_tag
from django.conf import settings
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()





urlpatterns = patterns('',
    ('^$', blog),
    ('^about/$', about),
    ('^(\d+)/$', cur_post),
    ('^tags/(\w+)/$', cur_tag),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)

