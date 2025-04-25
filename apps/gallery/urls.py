from django.contrib import admin
from django.urls import path
from apps.gallery.views import *

urlpatterns = [
    path('', index, name='index'),
]