from django.contrib import admin
from django.urls import path, include
from django.conf import Settings
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('idcheck/', views.idcheck, name='idcheck'),
    
]
 