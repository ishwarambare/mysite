from django.http import HttpResponse
from django.shortcuts import render
from .models import *


def home(request):
    return render(request, 'blog/home.html.j2')


def index(request):
    return HttpResponse("hello ishwar")


def post_list(request):
    post_list = Post.objects.all()
    return render(request, 'blog/blog.html.j2', {'post_list': post_list})
