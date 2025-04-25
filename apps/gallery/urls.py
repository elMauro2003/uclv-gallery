from django.contrib import admin
from django.urls import path
from apps.gallery.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', index, name='index'),
    path('login', login_view, name='login'),
    path('logout', LogoutView.as_view(),name='logout'),
]