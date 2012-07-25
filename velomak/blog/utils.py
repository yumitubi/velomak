# -*- coding: utf-8 -*-

from velomak.blog.models import Posts, Tags, Category

def get_posts():
    """return posts
    """
    return Posts.objects.all()

def get_post(url_post):
    """return post
    """
    return Posts.objects.get(id = url_post)

def get_tags():
    """return tags list
    """
    return Tags.objects.values_list('tag', flat=True)

def get_posts_tag(url_tag):
    """return posts from one tag
    """
    return Posts.objects.filter(tags__tag=url_tag)

def get_tag_to_post(id_post):
    """return tags for one post
    """
    tags = Posts.objects.get(id=id_post)
    list_tags =  [t.tag for t in tags.tags.all()]
    return list_tags

def get_posts_categ(categ):
    """return posts fron id_categ
    Arguments:
    - `self`:
    - `id_categ`: id category
    """
    return Posts.objects.filter(categories__categ=categ)

def get_categs():
    """return
    Arguments:
    - `self`:
    """
    return Category.objects.values_list('categ', flat=True)

def get_categories(self):
    """return categories
    """
    return set(get_categs())
