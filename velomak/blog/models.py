# -*- coding: utf-8 -*-
from django.db import models
from tinymce import models as tinymce_models


class Category(models.Model):
    categ = models.TextField(blank=True, null=True, unique=True)

    class Meta:
        app_label = 'velomak'
        db_table = 'categories'

    def __unicode__(self):
        return self.categ


class Posts(models.Model):
    header = models.TextField( blank = True )
    post = tinymce_models.HTMLField( blank = True )
    prepost = tinymce_models.HTMLField( blank = True )
    date_pub = models.DateField( auto_now_add = True )
    tags = models.ManyToManyField('velomak.Tags')
    categories = models.ForeignKey('velomak.Category')

    def __unicode__(self):
        return self.header

    class Meta:
        ordering = ["-date_pub"]
        app_label = 'velomak'
        db_table = 'posts'

class Tags(models.Model):
    # Нет смысла держать пустые
    tag = models.CharField(blank=False, null=False, max_length=64, unique=True)

    class Meta:
        app_label = 'velomak'
        db_table = 'tags'

    def __unicode__(self):
        return self.categ
