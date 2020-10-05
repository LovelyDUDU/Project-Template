from django.contrib import admin
from django.urls import path, include
from django.conf import Settings
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    
]
 