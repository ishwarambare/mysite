from django.http import HttpResponse
from django.shortcuts import render
from .models import *


def post_list(request):
    post_list = Post.objects.all()
    print(post_list)
    return render(request, 'blog/post_list.html.j2', {'post': post_list})
