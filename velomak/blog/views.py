# -*- coding: utf-8 -*-
from django.template import RequestContext
from django.http import Http404
from django.shortcuts import render_to_response
from forms import CommentForm
from velomak.blog.utils import get_posts, get_tags, get_categs, get_posts_categ, get_posts_tag, get_tag_to_post, get_post, get_posts_section, get_sections, get_categs_section, save_comment, get_comments, add_capcha_code, search_in_db
import capcha


def blog(request):
    """
    Основная Вьюха на главной странице
    """
    current_page = u"Главная страница"
    header_list = get_posts()
    meta = "блог le087 emacs linux python django"
    tags_obr = get_tags()
    categ_obr = get_categs()
    cloud_tags = get_tags()
    section_posts = get_sections()
    return render_to_response('titul.html', {
        'current_page':current_page,
        'header_list':header_list,
        'tags_obr':tags_obr,
        'categ_obr':categ_obr,
        'cloud_tags':cloud_tags,
        'meta':meta,
        'section_posts':section_posts,
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
        raise Http404
    valid_add_comment = False
    meta = tags_obr = get_tag_to_post(offset)
    header_post = get_post(current_page)
    if header_post == False:
        current_page = 'Страница не найдена'
        return render_to_response('404.html', {
                'current_page':current_page,
                'meta':meta,
                }, context_instance = RequestContext(request))
    categ_obr = get_categs()
    cloud_tags = get_tags()
    section_posts = get_sections()
    comments = get_comments(current_page)
    cap = capcha.capcha()
    name_capcha, code_capcha = cap.gen_capcha()
    add_capcha_code(name_capcha, code_capcha)
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            valid_add_comment = save_comment({'author':comment_form.cleaned_data['author'],
                                              'email':comment_form.cleaned_data['email'],
                                              'message':comment_form.cleaned_data['message'],
                                              'post':current_page,
                                              'delete':False,
                                              'capcha_code':comment_form.cleaned_data['valid'],
                                              })
            from django.core.mail import send_mail
            send_mail(comment_form.cleaned_data['author'], 
                      u'Новый комментарий на сайте: \n\n' + comment_form.cleaned_data['message'], 
                      'mak.tomilov@yandex.ru', ['mak.tomilov@gmail.com'], 
                      fail_silently=False)
            if valid_add_comment == False:
                comment_form = CommentForm()
    else:
        comment_form = CommentForm()
    return render_to_response('post.html', {
        'current_page':current_page,
        'header_post':header_post,
        'tags_obr':tags_obr,
        'categ_obr':categ_obr,
        'cloud_tags':cloud_tags,
        'meta':meta,
        'section_posts':section_posts,
        'comment_form':comment_form,
        'comments':comments,
        'name_capcha':name_capcha,
        'valid_add_comment':valid_add_comment
        }, context_instance = RequestContext(request))

def cur_tag(request, offset):
    """Отображает список материалов по выбранному тегу
    Arguments:
    - `request`:
    - `offset`:
    """
    current_page = u"Материалы по тегу: " + offset
    offset_without_earth = offset.replace('_', ' ')
    meta = "блог le087 emacs linux python django"
    header_list = get_posts_tag(offset_without_earth)
    tags_obr = get_tags()
    categ_obr = get_categs()
    cloud_tags = get_tags()
    section_posts = get_sections()
    return render_to_response('titul.html', {
            'current_page':current_page,
            'header_list':header_list,
            'tags_obr':tags_obr,
            'categ_obr':categ_obr,
            'cloud_tags':cloud_tags,
            'meta':meta,
            'section_posts':section_posts 
            }, context_instance = RequestContext(request))

def cur_categ(request, offset):
    """Отображает материалы по текущей категории
    Arguments:
    - `request`:
    - `offset`:
    """
    current_page = u"Материалы по категории: " + offset
    offset_without_earth = offset.replace('_', ' ')
    meta = "блог le087 emacs linux python django"
    header_list = get_posts_categ(offset_without_earth)
    # categ_obr - получаем категории, которые принадлежат
    # только к определенной категории
    if header_list and header_list[0].section: 
        categ_obr = get_categs_section(header_list[0].section) 
    else:
        categ_obr = get_categs()
    tags_obr = get_tags()
    cloud_tags = get_tags()
    section_posts = get_sections()
    return render_to_response('titul.html', {
        'current_page':current_page,
        'header_list':header_list,
        'categ_obr':categ_obr,
        'tags_obr':tags_obr,
        'cloud_tags':cloud_tags,
        'meta':meta,
        'section_posts':section_posts 
        }, context_instance = RequestContext(request))

def cur_section(request, offset):
    """ Обображает материалы для конкретной секции
    """
    current_page = u"Материалы в разделе: " + offset
    offset_without_earth = offset.replace('_', ' ')
    meta = "блог le087 emacs linux python django"
    header_list = get_posts_section(offset_without_earth)
    categ_obr = get_categs_section(offset_without_earth)
    tags_obr = get_tags()
    cloud_tags = get_tags()
    section_posts = get_sections()
    return render_to_response('titul.html', {
        'current_page':current_page,
        'header_list':header_list,
        'categ_obr':categ_obr,
        'tags_obr':tags_obr,
        'cloud_tags':cloud_tags,
        'meta':meta,
        'section_posts':section_posts
        }, context_instance = RequestContext(request))
    
def search(request):
    """return results for search 
    Arguments:
    - `request`:
    """
    meta = "блог le087 emacs linux python django"
    current_page = "Результаты поиска"
    section_posts = get_sections()
    cloud_tags = get_tags()
    categ_obr = get_categs()
    if request.method == 'POST':
        header_list = list(set(search_in_db(request.POST['search'])))
    else:
        header_list = []
    return render_to_response('titul.html', {
        'current_page':current_page,
        'meta':meta,
        'section_posts':section_posts,
        'categ_obr':categ_obr,
        'cloud_tags':cloud_tags,
        'header_list':header_list
        }, context_instance = RequestContext(request))
 
