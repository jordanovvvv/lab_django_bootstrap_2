from .models import BlogComment, BlogPost
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = BlogComment
        fields = ('author', 'content')


class PostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs["class"] = "form-control"

    class Meta:
        model = BlogPost
        exclude = ("author",)
