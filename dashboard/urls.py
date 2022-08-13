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

    # Manage Leader
    path('manage_leader/', views.manage_leader, name='manage_leader'),
    path('update_leader/<int:id>', views.update_leader, name='update_leader'),

    # Manage Awards
    path('manage_awards/', views.manage_awards, name='manage_awards'),
    path('update_awards/<int:id>', views.update_awards, name='update_awards'),
    path('delete_awards/<int:id>', views.delete_awards, name='delete_awards'),
]