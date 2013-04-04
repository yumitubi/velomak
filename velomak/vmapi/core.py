# -*- coding: utf-8 -*-
"""
Данный файл содержит несколько фукнкций, позволяющих осуществлять следующие
основные операции:

--> Секция Getting - получение списка постов, тегов, категорий, секций
--> Секция Adding - добавление новых постов, тегов, категорий, секций
--> Секция Delete - удаление постов, тегов, категорий, секций
--> Секция Replacing - замена, правка 
--> Секция Comments - работа с комментариями

"""


from velomak.settings import DIR_CACHE, DIR_CAPCHA
from velomak.blog.models import Posts, Tags, Category, Section, Comms, Capcha
from velomak.blog.utils import get_tags

    


