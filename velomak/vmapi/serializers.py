# -*- coding: utf-8 -*-


from rest_framework import serializers
from velomak.blog.models import Category, Tags


class CategSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'categ', 'enabled', 'weight', 'section')


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = ('id', 'tag')
