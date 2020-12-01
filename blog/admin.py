from django.contrib import admin

from blog.models import *


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    fields = ['title', 'slug', 'author', 'body', 'image']
    list_display = ['title', 'author', 'publish', 'status']
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'created', 'active')
    # list_display_links = ['email']
    # list_editable = ['name','post']
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')
