from django.shortcuts import render
from django.views.generic import ListView
from . import views

from .models import BlogPost, Comment

class PostList(ListView):
    """view to create the post on the blog"""
    model = BlogPost
    template_name = 'blog/blog.html'
  
    paginate_by = 6

