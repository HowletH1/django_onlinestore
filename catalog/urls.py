from django.urls import path

from catalog.apps import CatalogConfig
from . import views

app_name = CatalogConfig.name

urlpatterns = [
    path('', views.ProductList.as_view()),
    path('contacts/', views.ProductContact.as_view()),
    path('product/<int:pk>/', views.ProductDetails.as_view(), name='product')
]
