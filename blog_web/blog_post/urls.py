from django.contrib import admin
from django.urls import path
from . import views

app_name='blog_web'

urlpatterns=[
    path('', views.index, name='blog_index'),
]