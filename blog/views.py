from django.shortcuts import render
from . import views
from .models import BlogPost, Comment

def post_list(request):
    post_list = BlogPost.objects.all()

    return render(request, 'blog/blog.html')


