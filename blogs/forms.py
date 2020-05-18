from django.forms import ModelForm
from.models import blog, comments


class CommentForm(ModelForm):
    class Meta:
        model = comments
        fields = ['comment_author', 'comment_body']