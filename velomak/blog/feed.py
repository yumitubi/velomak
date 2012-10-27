# -*- coding: utf-8 -*-

from django.contrib.syndication.views import Feed
from velomak.blog.models import Posts
from django.utils.feedgenerator import Rss201rev2Feed

class RSSFeed(Feed):
    feed_type = Rss201rev2Feed
    title = 'le087\'s blog'
    description = 'блог о linux, python, emacs и другом IT'
    link = '/'
    item_author_name = 'le087'

    def items(self):
        return Posts.objects.filter(not_publicate_main=0, flag_enabled=1).order_by('-date_pub')[:5]
    
    def item_description(self, post):
        return post.prepost

    def item_link(self, post):
        link = '/'+str(post.id)+'/'
        return link
