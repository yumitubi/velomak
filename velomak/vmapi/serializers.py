# -*- coding: utf-8 -*-


from django.forms import widgets
from rest_framework import serializers
from velomak.blog.models import Posts, Tags, Category, Comms, Capcha


class CategSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'categ', 'enabled', 'weight', 'section')
