from django.contrib import admin
from django.urls import path
from . import views
app_name='login'

urlpatterns=[
    path('', views.index),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin')
]