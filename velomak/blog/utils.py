# -*- coding: utf-8 -*-

import os, shutil, datetime, time
from velomak.settings import DIR_CACHE, DIR_CAPCHA
from velomak.blog.models import Posts, Tags, Category, Section, Comms, Capcha

def clear_cache(directory):
    """clear directory with cashe
    """
    if os.path.exists(directory):
        list_dirs = os.listdir(directory)
        try:
            for direct in list_dirs:
                shutil.rmtree(directory + direct)
            return True
        except:
            return False
    else:
        return False

def clear_capcha(directory, expire):
    """clear directory with capcha images"""
    now = datetime.datetime.now()
    now_sec = time.mktime(now.timetuple())
    list_capcha_images = os.listdir(DIR_CAPCHA)
    for image in list_capcha_images:
        ctime_file = os.path.getctime(DIR_CAPCHA + '/' + image)
        if now_sec-ctime_file > expire:
            # TODO сделать более адекватную обработку
            try:
                os.remove(DIR_CAPCHA + '/' + image)
            except:
                pass

def add_capcha_code(name_capcha, code_capcha):
    """ add communicate in database 
    between capcha image and capcha code
    """
    add_capcha_database = Capcha(picture_name=name_capcha,
                                 capcha_code=code_capcha,
                                 use=False)
    add_capcha_database.save()

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
    
def save_comment(dicti):
    """save comment from user
    Arguments:
    - `dicti`: data in database
    """
    # clear cache before add comment
    # in database
    if DIR_CACHE:
        clear_cache(DIR_CACHE)
    try:
        note = Capcha.objects.filter(capcha_code=dicti['capcha_code'])[0]
    except:
        note = False
    if note and note.use == False:  
        add_note = Comms(author=dicti['author'],
                         email=dicti['email'],
                         post_id=int(dicti['post']),
                         message=dicti['message'],
                         delete=dicti['delete']) 
        add_note.save()
        note.use = True
        note.save()
        #clear capcha images 
        clear_capcha(DIR_CAPCHA, 30)
        return False
    else:
        return True

def get_comments(id_post):
    """get all comments for one post
    
    Arguments:
    - `id_post`: id of post
    """
    return Comms.objects.filter(post__id=id_post)

