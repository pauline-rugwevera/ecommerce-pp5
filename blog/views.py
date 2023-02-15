from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from . import views

from .models import BlogPost, Comment

class PostList(ListView):
    """view to create the post on the blog"""
    model = BlogPost
    template_name = 'blog/blog.html'
  
    paginate_by = 6






def post_detail(request, slug):
    """renders post detail"""
    post = BlogPost.objects.filter(slug=slug).first()

    
    
    if request.method == "POST":

        body = request.POST.get('body', '')
       
    return render(request, "blog/post_detail.html",
                  {'post': post,})

