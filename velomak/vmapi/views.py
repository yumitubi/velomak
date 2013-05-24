# -*- coding: utf-8 -*-


from django.http import HttpResponse, Http404
# from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
# from rest_framework.parsers import JSONParser
from velomak.blog.models import Category, Tags
from velomak.vmapi.serializers import CategSerializer, TagSerializer


class JSONResponse(HttpResponse):
    """ return conten into JSON"""

    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@api_view(['GET', 'POST'])
def categ_list(request):
    """
    Возвращает список всех категорий
    """
    if request.method == 'GET':
        categs = Category.objects.all()
        serializer = CategSerializer(categs, many=True)
        return JSONResponse(serializer.data)
    return Http404


@api_view(['GET', 'POST'])
def tag_list(request):
    """
    Возвращает список все тагов
    """
    if request.method == 'GET':
        tags = Tags.objects.all()
        serializer = TagSerializer(tags, many=True)
        return JSONResponse(serializer.data)
    return Http404
