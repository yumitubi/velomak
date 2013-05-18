# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url


urlpatterns = patterns('vmapi.views',
    url(r'^api/$', 'categ_list'),
)
