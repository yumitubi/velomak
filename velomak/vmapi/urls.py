# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url


urlpatterns = patterns('vmapi.views',
    url(r'^api/categs/$', 'categ_list'),
    url(r'^api/tags/$', 'tag_list'),                       
)
