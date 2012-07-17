# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, url
urlpatterns = patterns('blog.views',
    url(r'^about/$', 'about', name='velomak-about'),
    url(r'^(?P<post_id>\d+)/$', 'cur_post', name='velomak-cur_post'),
    url(r'^tags/(?P<tag>[\w]+)/$', 'cur_categ', name='velomak-cur_categ'),
    url(r'^$', 'blog', name='velomak-blog'))
