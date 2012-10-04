# -*- coding: utf-8 -*-

from django import forms

class CommentForm(forms.Form):
    author = forms.CharField(label='Ваше имя:', max_length=100)
    email = forms.EmailField(label='E-mail:', max_length=100)
    message = forms.CharField(label='Комменатрий:', widget=forms.Textarea)
