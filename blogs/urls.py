from django.urls import path
from .views import BlogDetailView, find

urlpatterns = [
    path('detail/<int:pk>/', BlogDetailView, name='detail'),
    path('find/', find, name='find'),
]