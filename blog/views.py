from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from . import views
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import PostForm

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
   
    if request.method == "POST":
              
       user = request.user
       body = request.POST.get('body', '')
       comment = Comment(user=user, body=body, blog_id=post)
       comment.save()    
    return render(request, "post_detail.html",
                  {'post': post, 'comments': comments})

@login_required
def delete_comment(request, comment_id):
    """
    A view to delete comments by admin
    """
    if not request.user.is_superuser:
        messages.error(
            request, 'You are not authorized to perform this action!!')
        return redirect(
            reverse('blog'))

    comment = get_object_or_404(Comment, pk=comment_id)
    comment.delete()
    messages.success(request, 'The comment was removed!')
    return redirect(reverse('blog'))
    

@login_required
def editPost(request, slug):
    """
    A view for admin to edit blog posts 
    
    """
    if not request.user.is_superuser:
        messages.error(
            request, 'You are not authorized to perform this action!')
        return redirect(reverse('home'))

    post = get_object_or_404(BlogPost, slug=slug)
    if request.method == 'POST':
        postForm = PostForm(request.POST, request.FILES, instance=post)
        if postForm.is_valid():

            instance = postForm.save(commit=False)
          
            postForm.save()
            messages.success(request, 'Successfully updated the post!')
            return redirect('blog')
        else:
            messages.error(request, 'Failed to update the post. \
                Please ensure the form is valid.')
         
        
    else:
        postForm = PostForm(instance=post)
        messages.info(
            request, f'You are currently editing: {post.slug}')

    template = 'edit_post.html'
    context = {
        'postForm': postForm,
        'post': post,
    }

    return render(request, template, context)

@login_required
def deletePost(request, slug):
    """
    A view to delete posts
    """
    if not request.user.is_superuser:
        messages.error(
            request, 'You are not authorized to perform this action!!')
        return redirect(reverse('home'))

    post = get_object_or_404(BlogPost, slug=slug)
    post.delete()
    messages.success(request, 'The post was deleted!')
    return redirect(reverse('blog'))