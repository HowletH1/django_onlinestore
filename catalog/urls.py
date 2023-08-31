from django.urls import path

from catalog.apps import CatalogConfig
from . import views
from catalog.views import ProductCreate, ProductUpdate, ProductDelete

app_name = CatalogConfig.name

urlpatterns = [
    path('', views.ProductList.as_view(), name='list'),
    path('contacts/', views.ProductContact.as_view(), name='contacts'),
    path('product/<int:pk>/', views.ProductDetails.as_view(), name='product'),
    path('create/', ProductCreate.as_view(), name='product_create'),
    path('update/<int:pk>/', ProductUpdate.as_view(), name='product_update'),
    path('delete/<int:pk>/', ProductDelete.as_view(), name='product_delete'),
]
