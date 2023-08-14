from django.urls import path

from catalog.apps import CatalogConfig
from . import views

app_name = CatalogConfig.name

urlpatterns = [
    path('', views.home),
    path('contacts/', views.contacts),
    path('product/<int:pk>/', views.ProductDetails.as_view(), name='product')
]
