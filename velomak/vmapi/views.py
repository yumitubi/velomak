# -*- coding: utf-8 -*-

# from django.template import RequestContext
from django.http import HttpResponse
# from django.shortcuts import render_to_response
from velomak.blog.utils import get_tags, get_categs
import json


def api_tags(request):
    """return list tags

    Arguments:
    - `request`:
    """
    tags = get_tags()
    return HttpResponse(json.dumps(list(tags), 
                                   ensure_ascii=False, 
                                   encoding="utf-8"),
                        content_type="application/json")


def api_categs(request):
    """return list categories
    
    Arguments:
    - `request`:
    """
    categs = get_categs()
    return HttpResponse(json.dumps([c.categ for c in categs], 
                                   ensure_ascii=False, 
                                   encoding="utf-8"),
                        content_type="application/json")
    
