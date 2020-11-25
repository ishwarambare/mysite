from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import *

'''
def post_list(request):
    post_list1 = Post.objects.all()
    print(post_list)
    return render(request, 'blog/post_list.html.j2', {'post': post_list1})


def post_detail(request, id):
    post = get_object_or_404(Post, pk=id)
    print(post)
    return render(request,
                  'blog/detail.html.j2',
                  {'post': post})

'''

from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, \
    PageNotAnInteger
from django.views.generic import ListView
from .models import Post


def post_list(request):
    object_list = Post.published.all()
    paginator = Paginator(object_list, 3)  # 3 posts in each page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)
    return render(request, 'blog/post/list.html.j2', {'page': page, 'posts': posts})


# def post_detail(request, year, month, day, post,id):
def post_detail(request, id):
    # post = get_object_or_404(Post, slug=post,
    #                          status='published',
    #                          publish__year=year,
    #                          publish__month=month,
    #                          publish__day=day)

    post = get_object_or_404(Post, id=id)


    return render(request,
                  'blog/post/detail.html.j2',
                  {'post': post})


class PostListView(ListView):
    queryset = Post.published.all()
    print(queryset)
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html.j2'
