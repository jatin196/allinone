from django.urls import path
from .views import (BlogDetailView, BlogListView, Search, BlogAdd
# ,                   BlogDelete
    , BlogUpdate
 )


urlpatterns = [
    path('search/', Search, name='search'),
    path('list/', BlogListView.as_view(), name='list'),
    path('add/', BlogAdd.as_view(), name='add-blog'),

    path('detail/<int:pk>/', BlogDetailView, name='detail'),
    # path('detail/<int:pk>/delete', BlogDelete, name='blog-delete'),
    path('detail/<int:pk>/update', BlogUpdate, name='blog-update'),

    # path('find/', find, name='find'),
]