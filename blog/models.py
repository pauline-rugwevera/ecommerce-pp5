from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=130, unique=True)
    body = models.TextField()
    image = models.ImageField(null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title


class Comment(models.Model):
    """model for comments on blog posts """
    creator = models.CharField(max_length=80)
    body = models.TextField()
    blog_id = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} created by {self.name}"