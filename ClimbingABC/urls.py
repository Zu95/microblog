from django.urls import path
from . import views

urlpatterns = [
    path('/', views.index, name='index'),
    path('', views.index, name='index'),
    path('category/', views.index, name='index'),
    path('category/<int:category_id>', views.category, name='category'),
    path('category/<int:category_id>/post/<int:post_id>', views.category, name='category'),
]