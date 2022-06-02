from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import render
# Create your models here.
from django.template import RequestContext


class BlogPost(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blogposts")
    created_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    files = models.FileField(upload_to=None, max_length=200, null=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def image(request):
        imagefile = BlogPost()
        variables = RequestContext(request, {
            'imagefile': imagefile
        })
        return render('blogpost.html', variables)

class BlogComment(models.Model):
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.content, self.author)