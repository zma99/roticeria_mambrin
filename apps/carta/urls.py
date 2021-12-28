from os import name
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    #path('', views.base),
    path('menu/', views.menu),
    path('conocenos/', views.conocenos),
]