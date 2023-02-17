from django.shortcuts import render, redirect,reverse, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from . import views
from django.contrib import messages
from .forms import CommentForm
from django.contrib.auth.decorators import login_required


from .models import BlogPost, Comment

class PostList(ListView):
    """view to create the post on the blog"""
    model = BlogPost
    template_name = 'blog.html'
  
    paginate_by = 6


def post_detail(request, slug):
    """renders post detail"""
    post = BlogPost.objects.filter(slug=slug).first()
    comments = Comment.objects.filter(blog_id=post)
    # try

    if request.method == "POST":
              
       user = request.user
       body = request.POST.get('body', '')
       comment = Comment(user=user, body=body, blog_id=post)
       comment.save()
       body = request.POST.get('body', '')
    
       
    return render(request, "post_detail.html",
                  {'post': post, 'comments': comments})
  

