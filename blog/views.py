
from django.views import generic
from .models import BlogPost
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.models import User
from .forms import CommentForm
# Create your views here.

class BlogPostList(generic.ListView):
    queryset = BlogPost.objects.order_by('-created_on')
    template_name = 'blogpost.html'

class BlogPostDetail(generic.DetailView):
    model = BlogPost
    template_name = 'blogpost_detail.html'

class Profile(generic.DetailView):
    model = User
    template_name = 'profile.html'

def comment(request, slug):
    template_name = 'blogpost_detail.html'
    post = get_object_or_404(BlogPost, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            new_comment = comment_form.save(commit=False)

            new_comment.post = post

            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})