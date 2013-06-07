# -*- coding: utf-8 -*-

from django import forms
from markitup.widgets import MarkItUpWidget

class CommentForm(forms.Form):
    author = forms.CharField(label='Ваше имя:', max_length=100)
    email = forms.EmailField(label='E-mail:', max_length=100)
    #message = forms.CharField(label='Комменатрий:', widget=forms.Textarea)
    message = forms.CharField(label='Комменатрий:', widget=MarkItUpWidget())
    valid = forms.CharField(label='Вы робот?', max_length=30)

