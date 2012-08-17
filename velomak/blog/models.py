# -*- coding: utf-8 -*-
from django.db import models
from tinymce import models as tinymce_models

class Category(models.Model):
    categ = models.CharField(blank=True, null=False, max_length=64, unique=True)
    enabled = models.BooleanField()
    weight = models.IntegerField(default=1)
    
    def __unicode__(self):
        return self.categ

    class Meta:
        ordering = ["-weight"]

class Tags(models.Model):
    tag = models.CharField(blank=True, null=False, max_length=64, unique=True)

    def __unicode__(self):
        return self.tag

class Section(models.Model):
    section = models.CharField(null=True, max_length=64, unique=True)
    weight = models.IntegerField(default=1)
    enabled = models.BooleanField()

    def __unicode__(self):
        return self.section

    class Meta:
        ordering = ["weight"]

class Posts(models.Model):
    header = models.TextField( blank = True )
    post = tinymce_models.HTMLField( blank = True )
    prepost = tinymce_models.HTMLField( blank = True )
    date_pub = models.DateField( auto_now_add = True )
    tags = models.ManyToManyField(Tags)
    categories = models.ForeignKey(Category)
    flag_enabled = models.BooleanField()
    section = models.ForeignKey(Section, null=True)

    def __unicode__(self):
        return self.header

    class Meta:
        ordering = ["-date_pub"]

class Files(models.Model):
    title = models.CharField(max_length=100)
    discription = models.TextField( blank = True )
    files = models.FileField(upload_to='files')

    def __unicode__(self):
        return self.title
