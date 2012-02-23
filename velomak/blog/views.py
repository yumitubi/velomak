# -*- coding: utf-8 -*-
from django.http import HttpResponse, Http404
from django.http import HttpResponseRedirect
from django.template import Template, Context
from django.shortcuts import render_to_response
from velomak.blog.models import Posts, Category, Comments

def blog(request):
    """
    Основная Вьюха на главной странице
    """
    current_page = "Главная страница"
    posts = Posts()
    header_list = posts.get_posts()
    tags_obr = posts.get_tags()
    return render_to_response('titul.html', {'current_page':current_page,
                                             'header_list':header_list,
                                             'tags_obr':tags_obr})

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
    header_post = post.get_post(current_page)
    return render_to_response('post.html', {'current_page':current_page,
                                             'header_post':header_post})

def about(request):
    """Возвращает страницу About
    """
    current_page = "Об авторе"
    return render_to_response('about.html', {'current_page':current_page})
    
