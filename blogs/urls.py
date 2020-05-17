from django.urls import path
from .views import BlogDetailView

urlpatterns = [
    path('detail/<int:pk>/', BlogDetailView.as_view(), name='detail')
]