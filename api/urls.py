from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.ProductList.as_view(), name='home'), #list all products in GET and create new in POST
    path('products/<int:pk>/', views.ProductDetailUpdate.as_view(), name='crud'), #retrieve single in GET, edit in PUT ,and destroy in delete
    path('products/create/', views.ProductCreate.as_view(), name='create'),
    path('products/list/', views.ProductListView.as_view(), name='list'),
    path('products/update/<int:pk>/', views.ProductUpdate.as_view(), name='update'),
    path('products/delete/<int:pk>/', views.ProductDelete.as_view(), name='delete'),
    path('products/detail/<int:pk>/', views.ProductDetail.as_view(), name='detail'),

]
