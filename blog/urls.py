from django.urls import path

from blog.apps import BlogConfig

from blog.views import BlogCreate, BlogList, BlogDetail, BlogUpdate, BlogDelete

app_name = BlogConfig.name

urlpatterns = [
    path('create/', BlogCreate.as_view(), name='create'),
    path('', BlogList.as_view(), name='list'),
    path('view/<int:pk>', BlogDetail.as_view(), name='view'),
    path('edit/<int:pk>', BlogUpdate.as_view(), name='edit'),
    path('delete/<int:pk>', BlogDelete.as_view(), name='delete'),
]
