from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('index/', views.index),
    path('home/', views.home),
    path('mylist/', views.mylist),
    path('upload/', views.upload),
    path('login/', views.loginpage),
    path('logout/', views.logoutpage),
    path('register/', views.register),
]