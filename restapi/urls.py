from django.contrib import admin
from django.urls import path, include
from restapi import views

urlpatterns = [
    path('sliderList/', views.sliderList, name='sliderList'),
]