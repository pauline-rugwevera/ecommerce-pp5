from django.contrib import admin

from .models import BlogPost, Comment

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    
    list_display = ('title', 'slug', 'created_on')
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('created_on',)


@admin.register(Comment)
class Comment(admin.ModelAdmin):
    list_display = ('creator', 'body', 'blog_id', 'created_on',)
    list_filter = ('created_on',)
    search_fields = ('name', 'body')