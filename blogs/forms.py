from django.forms import ModelForm
from.models import blog, comments


class CommentForm(ModelForm):
    class Meta:
        model = comments
        fields = ['comment_author', 'comment_body']

class BlogForm(ModelForm):
    class Meta:
        model = blog
        fields = ['title', 'author', 'cover', 'content']