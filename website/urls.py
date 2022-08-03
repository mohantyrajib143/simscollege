from django.contrib import admin
from django.urls import path, include
from website import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('whyus/', views.whyus, name='whyus'),
    path('awards/', views.awards, name='awards'),
    path('science/', views.science, name='science'),
]