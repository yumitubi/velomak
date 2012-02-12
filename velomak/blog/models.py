from django.db import models

# import tagging
# from tagging.fields import TagField
# from tagging.models import Tag

class Posts(models.Model):
    header = models.TextField( blank = True )
    post = models.TextField( blank = True )
    prepost = models.TextField( blank = True )
    date_pub = models.DateField( auto_now_add = True)
    tags = models.TextField( blank = True )

class Category(models.Model):
    category = models.TextField( blank = True )
    id_post = models.IntegerField( default=0 )

class Coments(models.Model):
    autor = models.CharField(max_length=100)
    comment = models.TextField( blank = True )
    id_post = models.IntegerField( default=0 )
    date_pub = models.DateField()
