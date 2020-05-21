from django.db import models
from tinymce.models import HTMLField

class comments(models.Model):
    Blog = models.ForeignKey('blog', on_delete=models.CASCADE, related_name='Comment')
    comment_author = models.CharField(max_length=35)
    timestamp = models.DateTimeField(auto_now_add=True)
    comment_body =  HTMLField()
    def __str__(self):
        return "Comment by : {name}".format(name=self.comment_author)

categories = [
    ( 'Web Design', 'webd'),
    ('Travel', 'travel'),
    ( 'Food', 'food'),
    ('Other', 'other')
]
class blog(models.Model):
    title = models.CharField(max_length=65)
    content = HTMLField('Content')
    # content = models.TextField()
    author = models.CharField(max_length=35)
    cover = models.ImageField(null=True, blank=True)
    category =  models.CharField(
        max_length=10,
        choices=categories,
        default='webd',
        null=True,
        blank=True
    )
    def __str__(self):
        return "Blog : {name}".format(name=self.title)
    def desc(self):
        # array = self.content.split(" ")
        # return " ".join(array[:10])
        return self.content[:120]

    def commentCount(self):
        return self.Comment.count()
