from cgitb import text
from dataclasses import field
from pyexpat import model
from urllib import request
from django import forms

from .models import Forum

class ForumForm(forms.ModelForm):
    class Meta:
        model = Forum
        fields = ['text' ]
        labels = {'text': 'text' }