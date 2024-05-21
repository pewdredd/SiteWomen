from django.contrib import admin
from django.urls import path

from . import views

app_name = 'women'

urlpatterns = [
    path('', views.index_view, name='index')
]

