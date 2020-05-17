from django.db import models

class blog(models.Model):
    title = models.CharField(max_length=65)
    content = models.TextField()
    author = models.CharField(max_length=35)

