from django.db import models

class blog(models.Model):
    title = models.CharField(max_length=65)
    content = models.TextField()
    author = models.CharField(max_length=35)
    cover = models.ImageField(null=True, blank=True)


class comments(models.Model):
    comment_author = models.CharField(max_length=35)
    timestamp = models.DateTimeField(auto_now_add=True)
    comment_body = models.TextField()
