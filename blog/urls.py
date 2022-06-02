from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.BlogPostList.as_view(), name='blogpost'),
    path('', views.Profile.as_view(), name='profile'),
    path('<slug:slug>/', views.BlogPostDetail.as_view(), name='blogpost_detail'),
]