from django.contrib import admin

from blog.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'publish', 'status']
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')


