from django.db import models

class blog(models.Model):
    title = models.CharField(max_length=65)
    content = models.TextField()
    author = models.CharField(max_length=35)
    cover = models.ImageField(null=True, blank=True)
    def __str__(self):
        return "Blog : {name}".format(name=self.title)
    def desc(self):
        # array = self.content.split(" ")
        # return " ".join(array[:10])
        return self.content[:120]

class comments(models.Model):
    Blog = models.ForeignKey(blog, on_delete=models.CASCADE, related_name='Comment')
    comment_author = models.CharField(max_length=35)
    timestamp = models.DateTimeField(auto_now_add=True)
    comment_body = models.TextField()
    def __str__(self):
        return "Comment by : {name}".format(name=self.comment_author)

