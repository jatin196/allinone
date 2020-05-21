from django.forms import ModelForm
from django import forms
# from tinymce.widgets import TinyMCE
from.models import blog, comments

#
# class TinyMCEWidget(TinyMCE):
#     def use_required_attribute(self, *args):
#         return False


class CommentForm(forms.ModelForm):
    class Meta:
        model = comments
        fields = ['comment_author', 'comment_body']

class BlogForm(forms.ModelForm):
    # content = forms.CharField(required=False, widget=forms.Textarea(attrs={'class':'notrequired'}))
    class Meta:
        model = blog
        fields = ['title', 'author', 'cover','category', 'content']