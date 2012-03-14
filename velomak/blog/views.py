# -*- coding: utf-8 -*-
from django.http import HttpResponse, Http404
from django.http import HttpResponseRedirect
from django.template import RequestContext, Template, Context 
from django.shortcuts import render_to_response
from velomak.blog.models import Posts, Category, Comments

def blog(request):
    """
    Основная Вьюха на главной странице
    """
    current_page = "Главная страница"
    posts = Posts()
    categ = Category()
    header_list = posts.get_posts()
    tags_obr = posts.get_tags()
    categories = categ.get_categories()
    return render_to_response('titul.html', {'current_page':current_page,
                                             'header_list':header_list,
                                             'tags_obr':tags_obr,
                                             'categories':categories},
                               context_instance = RequestContext(request))

def cur_post(request, offset):
    """Отображает один пост по URL
    
    Arguments:
    - `request`: 
    - `offset`: урл из адресной строки
    """
    try:
        current_page = int(offset)
    except:
        pass
    post = Posts()
    tags_obr = post.get_tag_to_post(offset)
    header_post = post.get_post(current_page)
    return render_to_response('post.html', {'current_page':current_page,
                                             'header_post':header_post,
                                             'tags_obr':tags_obr})

def cur_tag(request, offset):
    """Отображает список материалов по выбранному тегу
    
    Arguments:
    - `request`:
    - `offset`:
    """
    current_page = u'Материалы по тегу: ' + offset
    offset_without_earth = offset.replace('_', ' ')
    posts = Posts()
    header_list = posts.get_posts_tag(offset_without_earth)
    tags_obr = posts.get_tags()
    if header_list:
        return render_to_response('titul.html', {'current_page':current_page,
                                                 'header_list':header_list,
                                                 'tags_obr':tags_obr})
    else:
        current_page = "Об авторе"
        return render_to_response('about.html', {'current_page':current_page})

    
def about(request):
    """Возвращает страницу About
    """
    current_page = "Об авторе"
    return render_to_response('about.html', {'current_page':current_page})
    
