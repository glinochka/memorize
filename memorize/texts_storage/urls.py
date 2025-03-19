from django.urls import path
from . import views

urlpatterns = [
    path('add', views.new_text, name='add'),
    path('listof_texts', views.listof_texts, name='list'),
    path('read', views.read_text, name='read'),
]