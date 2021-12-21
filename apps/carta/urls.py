from os import name
from django.urls import path

from . import views

urlpatterns = [
    path('', views.base),
    path('index/', views.index),
    path('menu/', views.menu),
]