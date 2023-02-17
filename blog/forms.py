from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import BlogPost


class PostForm(forms.ModelForm):
    """
    Form for adding a blog post
    """
    class Meta:
        model = BlogPost
        widgets = {
            'body': SummernoteWidget()
        }
        fields = [
            'title',
            'slug',
            'body',
            'image',
        ]

