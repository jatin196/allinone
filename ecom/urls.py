from django.urls import path
from .views import ProductList, ProductDetail
app_name = 'ecom'
urlpatterns = [
    path('', ProductList.as_view(), name='list'),
    path('detail/<int:pk>/', ProductDetail.as_view(), name='detail'),

]