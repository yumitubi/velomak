# -*- coding: utf-8 -*-
from django.db import models
from tinymce import models as tinymce_models
# from markitup.fields import MarkupField

class Section(models.Model):
    section = models.CharField(blank=True, null=True, max_length=64, unique=True)
    weight = models.IntegerField(default=1)
    enabled = models.BooleanField()

    def __unicode__(self):
        return self.section

    class Meta:
        ordering = ["weight"]

class Category(models.Model):
    categ = models.CharField(blank=True, null=False, max_length=64, unique=True)
    enabled = models.BooleanField()
    weight = models.IntegerField(default=1)
    section = models.ForeignKey(Section, blank=True, null=True)
    
    def __unicode__(self):
        return self.categ

    class Meta:
        ordering = ["-weight"]

class Tags(models.Model):
    tag = models.CharField(blank=True, null=False, max_length=64, unique=True)

    def __unicode__(self):
        return self.tag

class Posts(models.Model):
    header = models.TextField( blank = True )
    # post = MarkupField( blank = True )
    # prepost = MarkupField( blank = True )
    post = tinymce_models.HTMLField( blank = True )
    prepost = tinymce_models.HTMLField( blank = True )
    date_pub = models.DateTimeField()
    tags = models.ManyToManyField(Tags)
    categories = models.ForeignKey(Category)
    flag_enabled = models.BooleanField()
    not_publicate_main = models.BooleanField()
    section = models.ForeignKey(Section, blank=True, null=True)

    def __unicode__(self):
        return self.header

    def get_count_comments(self):
        """ return count comment for one post
        """
        return self.comms_set.count()

    class Meta:
        ordering = ["-date_pub"]

class Files(models.Model):
    title = models.CharField(max_length=100)
    discription = models.TextField( blank = True )
    files = models.FileField(upload_to='files')

    def __unicode__(self):
        return self.title

class Comms(models.Model):
    author = models.CharField(blank=True, null=True, max_length=100)
    email = models.CharField(blank=True, null=True, max_length=100)
    post = models.ForeignKey(Posts)
    message = models.TextField( blank = True )
    datatime = models.DateTimeField(auto_now_add=True)
    delete = models.BooleanField()
    
    def __unicode__(self):
        return self.author

    class Meta:
        ordering = ["datatime"]

class Capcha(models.Model):
    picture_name = models.CharField(blank=True, null=True, max_length=10)
    capcha_code = models.CharField(blank=True, null=True, max_length=10)
    use = models.BooleanField()
        
    def __unicode__(self):
        return self.picture_name

