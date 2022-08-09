from django.contrib import admin
from django.urls import path, include
from dashboard import views

urlpatterns = [
    path('', views.login, name='login'),
    path('forgot_pass/', views.forgot_pass, name='forgot_pass'),
]