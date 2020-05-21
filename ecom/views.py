from django.shortcuts import render
from django.views import generic
from .models import product


class ProductList(generic.ListView):
    model = product
    template_name = 'ecommerce/list.html'
    context_object_name = 'products'


class ProductDetail(generic.DetailView):
    model = product
    template_name = 'ecommerce/detail.html'
    context_object_name = 'product'


