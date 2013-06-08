# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, include, url
from velomak.blog.views import blog, cur_post, cur_tag, cur_categ, cur_section, search
from django.conf import settings
from blog.feed import RSSFeed
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    ('^$', blog),
    ('^(\d+)/$', cur_post),
    ('^tags/([\d\w\-_]+)/$', cur_tag),
    ('^categories/([\d\w\-_]+)/$', cur_categ),
    ('^section/([\d\w\-_]+)/$', cur_section),
    ('^search/$', search),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    url(r'^feed/?$', RSSFeed()),
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)

