from django import forms
from .models import *


class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False,
                               widget=forms.Textarea)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        # fields = ('title', 'author', 'image', 'body', 'status','publish','')
        fields = "__all__"



class PostFormNew(forms.ModelForm):
    class Meta:
        model=Post
        fields='__all__'
