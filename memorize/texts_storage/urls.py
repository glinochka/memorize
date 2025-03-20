from django.urls import path
from . import views

urlpatterns = [
    path('add', views.new_article, name='add'),
    path('listof_articles', views.listof_articles, name='list'),
    path('read', views.read_article, name='read'),
]