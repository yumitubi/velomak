# -*- coding: utf-8 -*-
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from velomak.blog.utils import get_posts, get_tags, get_categs, get_posts_categ, get_posts_tag, get_tag_to_post, get_post

def blog(request):
    """
    Основная Вьюха на главной странице
    """
    current_page = u"Главная страница"
    header_list = get_posts()
    tags_obr = get_tags()
    # assert False
    categ_obr = get_categs()
    cloud_tags = get_tags()
    return render_to_response('titul.html', {
        'current_page':current_page,
        'header_list':header_list,
        'tags_obr':tags_obr,
        'categ_obr':categ_obr,
        'cloud_tags':cloud_tags
        }, context_instance = RequestContext(request))

def cur_post(request, offset):
    """Отображает один пост по URL
    Arguments:
    - `request`: 
    - `offset`: урл из адресной строки
    """
    try:
        current_page = int(offset)
    except:
        # Если запрашивается некорректный номер страницы,
        # то перебрасываем на заглавную
        HttpResponseRedirect(reverse(u'velomak-blog'))
    tags_obr = get_tag_to_post(offset)
    header_post = get_post(current_page)
    categ_obr = get_categs()
    cloud_tags = get_tags()
    return render_to_response('post.html', {
        'current_page':current_page,
        'header_post':header_post,
        'tags_obr':tags_obr,
        'categ_obr':categ_obr,
        'cloud_tags':cloud_tags 
        }, context_instance = RequestContext(request))

def cur_tag(request, offset):
    """Отображает список материалов по выбранному тегу
    Arguments:
    - `request`:
    - `offset`:
    """
    current_page = u"Материалы по тегу: " + offset
    offset_without_earth = offset.replace('_', ' ')
    header_list = get_posts_tag(offset_without_earth)
    tags_obr = get_tags()
    categ_obr = get_categs()
    cloud_tags = get_tags()
    if header_list:
        return render_to_response('titul.html', {
            'current_page':current_page,
            'header_list':header_list,
            'tags_obr':tags_obr,
            'categ_obr':categ_obr,
            'cloud_tags':cloud_tags 
            }, context_instance = RequestContext(request))
    else:
        current_page = u"Об авторе"
        return render_to_response('about.html', {
            'current_page':current_page
            }, context_instance = RequestContext(request))

def cur_categ(request, offset):
    """Отображает материалы по текущей категории
    Arguments:
    - `request`:
    - `offset`:
    """
    current_page = u"Материалы по категории: " + offset
    offset_without_earth = offset.replace('_', ' ')
    header_list = get_posts_categ(offset_without_earth)
    categ_obr = get_categs()
    tags_obr = get_tags()
    cloud_tags = get_tags()
    if header_list:
        return render_to_response('titul.html', {
            'current_page':current_page,
            'header_list':header_list,
            'categ_obr':categ_obr,
            'tags_obr':tags_obr,
            'cloud_tags':cloud_tags 
            }, context_instance = RequestContext(request))
    else:
        current_page = "Об авторе"
        return render_to_response('about.html', {
            'current_page':current_page
            }, context_instance = RequestContext(request))
    
def about(request):
    """Возвращает страницу About
    """
    current_page = "Об авторе"
    return render_to_response('about.html', {
        'current_page':current_page
        }, context_instance = RequestContext(request))
    
