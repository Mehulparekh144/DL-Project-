from django.contrib import admin
from django.urls import path
from predictapp import views

urlpatterns = [
    path('form', views.form, name='form'),
    path('result', views.result, name='result'),


]
