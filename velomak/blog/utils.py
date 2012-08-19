# -*- coding: utf-8 -*-

from velomak.blog.models import Posts, Tags, Category, Section

def get_posts():
    """return posts
    """
    return Posts.objects.filter(not_publicate_main=0)

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
    return Category.objects.all()

def get_posts_section(sect):
    """return posts from one section
    """
    return Posts.objects.filter(section__section=sect)

def get_sections():
    """ return sections for template
    """
    return Section.objects.all()

def get_categs_section(sect):
    """return list categories for one section
    Arguments:
    - `sect`: current section
    """
    return Category.objects.filter(section__section=sect)
    
