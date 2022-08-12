from django.contrib import admin
from django.urls import path, include
from dashboard import views

urlpatterns = [
    path('', views.login, name='login'),
    path('forgot_pass/', views.forgot_pass, name='forgot_pass'),
    path('index/', views.dashboard, name='dashboard'),

    # Manage Slider
    path('manage_slider/', views.manage_slider, name='manage_slider'),
    path('update_slider/<int:id>', views.update_slider, name='update_slider'),
    path('update_slider_status/<int:id>', views.update_slider_status, name='update_slider_status'),
    path('delete_slider/<int:id>', views.delete_slider, name='delete_slider'),

    # Manage About Us
    path('manage_aboutus/', views.manage_aboutus, name='manage_aboutus'),
    path('update_aboutus/', views.update_aboutus, name='update_aboutus'),
]