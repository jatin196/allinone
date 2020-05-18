from django.contrib import admin
from .models import blog, comments
# Register your models here.

admin.site.register(blog)
admin.site.register(comments)