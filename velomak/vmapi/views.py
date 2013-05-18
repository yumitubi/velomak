# -*- coding: utf-8 -*-

from django.http import HttpResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
# from rest_framework.parsers import JSONParser
from velomak.blog.models import Category
from velomak.vmapi.serializers import CategSerializer

class JSONResponse(HttpResponse):

    def __init__(self, data, **kwargs):
        """
        
        Arguments:
        - `self`:
        - `data`:
        - `**kwargs`:
        """
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self.__init__(content, **kwargs))


@csrf_exempt
def categ_list(request):
    """
    Возвращает список всех категорий

    Arguments:
    - `request`:
    """
    if request.method == 'GET':
        categs = Category.objects.all()
        serializer = CategSerializer(categs, many=True)
        return JSONResponse(serializer.data)
    return Http404
