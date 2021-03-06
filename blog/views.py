from django.db.models import Count
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import send_mail
from django.views import View
from django.views.generic import ListView
from blog.models import *
from blog.forms import *
from taggit.models import Tag


def post_list(request, tag_slug=None):
    object_list = Post.published.all()
    tag = None

    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        object_list = object_list.filter(tags__in=[tag])

    paginator = Paginator(object_list, 2)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'blog/post/list.html.j2', {'page': page, 'posts': posts, 'tag': tag})


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                             status='published',
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)

    comments = post.comments.filter(active=True)
    new_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, 'blog/post/detail.html.j2', {'post': post,
                                                        'comments': comments,
                                                        'new_comment': new_comment,
                                                        'comment_form': comment_form, })


# class PostListView(ListView):
#     queryset = Post.published.all()
#     print(queryset)
#     context_object_name = 'posts'
#     paginate_by = 3
# template_name = 'blog/post/list.html.j2'


def post_share(request, post_id):
    post = get_object_or_404(Post, id=post_id, status='published')
    sent = False

    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = f"{cd['name']} recommends you read {post.title}"
            message = f"Read {post.title} at {post_url}\n\n" \
                      f"{cd['name']}\'s comments: {cd['comments']}"
            send_mail(subject, message, 'admin@myblog.com', [cd['to']])
            sent = True
            return render(request, 'blog/post/share.html.j2', {'post': post,
                                                               'form': form,
                                                               'sent': sent})

    else:
        form = EmailPostForm()
        return render(request, 'blog/post/share.html.j2', {'post': post,
                                                           'form': form,
                                                           'sent': sent})


def postform(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('blog:post_list'))
        else:
            return render(request, 'blog/form.html.j2', {'form': form})
    else:
        return render(request, 'blog/form.html.j2', {'form': form})


# class MyFormView(View):
#     form_class = PostForm
#     initial = {'key': 'value'}
#     template_name = 'blog/form.html.j2/'
#
#     def get(self, request, *args, **kwargs):
#         form = self.form_class(initial=self.initial)
#         return render(request, self.template_name, {'form': form})
#
#     def post(self, request, *args, **kwargs):
#         form = self.form_class(request.POST)
#         if form.is_valid():
#             form.save()
#             # return HttpResponseRedirect('/success/')
#             return HttpResponseRedirect(reverse('blog:post_list'))
#
#         return render(request, self.template_name, {'form': form})


def formdataview(request):
    form = PostFormNew()
    if request.method == 'POST':
        form = PostFormNew(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('blog:post_list'))
        else:
            return render(request, 'blog/form.html.j2', {'form': form})
    else:
        return render(request, 'blog/form.html.j2', {'form': form})
