from django.urls import path
from .views import BlogDetailView

urlpatterns = [
    path('detail/<int:pk>/', BlogDetailView, name='detail'),
    # path('find/', find, name='find'),
]