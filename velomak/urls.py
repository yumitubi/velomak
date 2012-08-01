# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, include, url
from velomak.blog.views import blog, cur_post, about, cur_tag, cur_categ
from django.conf import settings
from blog.feed import RSSFeed
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    ('^$', blog),
    ('^about/$', about),
    ('^(\d+)/$', cur_post),
    ('^tags/([\d\w\-_]+)/$', cur_tag),
    ('^categories/([\d\w\-_]+)/$', cur_categ),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    url(r'^feed/?$', RSSFeed()),
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    (r'^comments/', include('django.contrib.comments.urls')),
    (r'^tinymce/', include('tinymce.urls')),
)

