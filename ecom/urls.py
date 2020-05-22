from django.urls import path
from .views import (ProductList, ProductDetail, ProductCreate, ProductUpdate, AddToCart, Cart)
app_name = 'ecom'
urlpatterns = [
    path('', ProductList.as_view(), name='list'),
    path('add/', ProductCreate, name='create'),
    path('cart/', Cart, name='cart'),

    path('add-to-cart/<int:pk>/', AddToCart, name='add-to-cart'),

    path('detail/<int:pk>/', ProductDetail.as_view(), name='detail'),
    path('detail/<int:pk>/update/', ProductUpdate, name='update'),
]