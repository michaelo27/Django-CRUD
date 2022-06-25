from dataclasses import fields
from pyexpat import model
from re import M
from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            "title"
            "body"
        ]
