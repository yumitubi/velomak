# -*- coding: utf-8 -*-
from django.http import HttpResponse, Http404
from django.http import HttpResponseRedirect
from django.template import RequestContext, Template, Context 
from django.shortcuts import render_to_response
from velomak.blog.models import Posts, Category # , Comments

def blog(request):
    """
    Основная Вьюха на главной странице
    """
    current_page = "Главная страница"
    posts = Posts()
    categ = Category()
    header_list = posts.get_posts()
    tags_obr = posts.get_tags()
    categ_obr = categ.get_categs()
    cloud_tags = posts.cloud_tags()
    # categories = categ.get_categories()
    return render_to_response('titul.html', {'current_page':current_page,
                                             'header_list':header_list,
                                             'tags_obr':tags_obr,
                                             # 'categories':categories,
                                             'categ_obr':categ_obr,
                                             'cloud_tags':cloud_tags},
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
    categ = Category()    
    tags_obr = post.get_tag_to_post(offset)
    header_post = post.get_post(current_page)
    categ_obr = categ.get_categs()    
    return render_to_response('post.html', {'current_page':current_page,
                                             'header_post':header_post,
                                             'tags_obr':tags_obr,
                                             'categ_obr':categ_obr},
                               context_instance = RequestContext(request))

def cur_tag(request, offset):
    """Отображает список материалов по выбранному тегу
    
    Arguments:
    - `request`:
    - `offset`:
    """
    current_page = u'Материалы по тегу: ' + offset
    offset_without_earth = offset.replace('_', ' ')
    posts = Posts()
    categ = Category()
    header_list = posts.get_posts_tag(offset_without_earth)
    tags_obr = posts.get_tags()
    categ_obr = categ.get_categs()
    if header_list:
        return render_to_response('titul.html', {'current_page':current_page,
                                                 'header_list':header_list,
                                                 'tags_obr':tags_obr,
                                                 'categ_obr':categ_obr},
                               context_instance = RequestContext(request))
    else:
        current_page = "Об авторе"
        return render_to_response('about.html', {'current_page':current_page},
                               context_instance = RequestContext(request))

def cur_categ(request, offset):
    """Отображает материалы по текущей категории
    
    Arguments:
    - `request`:
    - `offset`:
    """
    current_page = u'Материалы по категории: ' + offset
    offset_without_earth = offset.replace('_', ' ')
    posts = Posts()
    categ = Category()
    header_list = posts.get_posts_categ(offset_without_earth)
    categ_obr = categ.get_categs()
    tags_obr = posts.get_tags()
    if header_list:
        return render_to_response('titul.html', {'current_page':current_page,
                                                 'header_list':header_list,
                                                 'categ_obr':categ_obr,
                                                 'tags_obr':tags_obr},
                               context_instance = RequestContext(request))
    else:
        current_page = "Об авторе"
        return render_to_response('about.html', {'current_page':current_page},
                               context_instance = RequestContext(request))
    


    
def about(request):
    """Возвращает страницу About
    """
    current_page = "Об авторе"
    return render_to_response('about.html', {'current_page':current_page},
                               context_instance = RequestContext(request))
    
