# -*- coding: utf-8 -*-


from django.http import Http404
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
from rest_framework.renderers import UnicodeJSONRenderer
from velomak.blog.models import Category, Tags
from velomak.vmapi.serializers import CategSerializer, TagSerializer


@api_view(['GET', 'POST'])
@renderer_classes((UnicodeJSONRenderer, ))
def categ_list(request):
    """
    return list all categs
    """
    if request.method == 'GET':
        categs = Category.objects.all()
        serializer = CategSerializer(categs, many=True)
        return Response(serializer.data)
    return Http404


@api_view(['GET', 'POST'])
@renderer_classes((UnicodeJSONRenderer, ))
def tag_list(request):
    """
    returt list all tags
    """
    if request.method == 'GET':
        tags = Tags.objects.all()
        serializer = TagSerializer(tags, many=True)
        return Response(serializer.data)
    return Http404
