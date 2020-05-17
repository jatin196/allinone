from django.shortcuts import render
from django.views import generic
from .models import blog

class BlogDetailView(generic.DetailView):
    model = blog
    template_name = 'blog/blog-detail.html'

