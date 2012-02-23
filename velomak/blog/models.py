# -*- coding: utf-8 -*-
from django.db import models

# import tagging
# from tagging.fields import TagField
# from tagging.models import Tag

class Posts(models.Model):
    header = models.TextField( blank = True )
    post = models.TextField( blank = True )
    prepost = models.TextField( blank = True )
    date_pub = models.DateField( auto_now_add = True)
    tags = models.TextField( True )

    def __unicode__(self):
        return self.header

    def get_posts(self):
        """return posts
        """
        return Posts.objects.all()

    def get_post(self, url_post):
        """return post
        """
        return Posts.objects.get(id = url_post)

    def get_tags(self):
        """return tags
        """
        tags = Posts.objects.all()
        list_tags = [[t.id, t.tags.split(',')] for t in tags]
        return list_tags
    
    class Meta:
        ordering = ["-date_pub"]

class Category(models.Model):
    category = models.TextField( blank = True )
    id_post = models.IntegerField( default=0 )

class Comments(models.Model):
    autor = models.CharField(max_length=100)
    comment = models.TextField( blank = True )
    id_post = models.IntegerField( default=0 )
    date_pub = models.DateField()
