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

    # Manage Student Testimonial
    path('manage_stdtestimonial/', views.manage_stdtestimonial, name='manage_stdtestimonial'),
    path('update_stdtestimonial/<int:id>', views.update_stdtestimonial, name='update_stdtestimonial'),
    path('update_stdtestimonial_status/<int:id>', views.update_stdtestimonial_status, name='update_stdtestimonial_status'),
    path('delete_stdtestimonial/<int:id>', views.delete_stdtestimonial, name='delete_stdtestimonial'),

    # Manage Alumni Testimonial
    path('manage_alumni_testimonial/', views.manage_alumni_testimonial, name='manage_alumni_testimonial'),
    path('update_alumni_testimonial/<int:id>', views.update_alumni_testimonial, name='update_alumni_testimonial'),
    path('update_alumni_testimonial_status/<int:id>', views.update_alumni_testimonial_status, name='update_alumni_testimonial_status'),
    path('delete_alumni_testimonial/<int:id>', views.delete_alumni_testimonial, name='delete_alumni_testimonial'),

    # Manage chse faculty
    path('manage_chse_faculty/', views.manage_chse_faculty, name='manage_chse_faculty'),
    path('update_chse_faculty/<int:id>', views.update_chse_faculty, name='update_chse_faculty'),
    path('update_chse_faculty_status/<int:id>', views.update_chse_faculty_status, name='update_chse_faculty_status'),
    path('delete_chse_faculty/<int:id>', views.delete_chse_faculty, name='delete_chse_faculty'),

    # Manage entrance faculty
    path('manage_entrance_faculty/', views.manage_entrance_faculty, name='manage_entrance_faculty'),
    path('update_entrance_faculty/<int:id>', views.update_entrance_faculty, name='update_entrance_faculty'),
    path('update_entrance_faculty_status/<int:id>', views.update_entrance_faculty_status, name='update_entrance_faculty_status'),
    path('delete_entrance_faculty/<int:id>', views.delete_entrance_faculty, name='delete_entrance_faculty'),

    # Manage college infrastructure
    path('manage_college/', views.manage_college, name='manage_college'),
    path('update_college/<int:id>', views.update_college, name='update_college'),
    path('update_college_status/<int:id>', views.update_college_status, name='update_college_status'),
    path('delete_college/<int:id>', views.delete_college, name='delete_college'),

    # Manage hostel infrastructure
    path('manage_hostel/', views.manage_hostel, name='manage_hostel'),
    path('update_hostel/<int:id>', views.update_hostel, name='update_hostel'),
    path('update_hostel_status/<int:id>', views.update_hostel_status, name='update_hostel_status'),
    path('delete_hostel/<int:id>', views.delete_hostel, name='delete_hostel'),

    # Manage gallery infrastructure
    path('manage_gallery/', views.manage_gallery, name='manage_gallery'),
    path('update_gallery/<int:id>', views.update_gallery, name='update_gallery'),
    path('update_gallery_status/<int:id>', views.update_gallery_status, name='update_gallery_status'),
    path('delete_gallery/<int:id>', views.delete_gallery, name='delete_gallery'),

    # Manage labs infrastructure
    path('manage_labs/', views.manage_labs, name='manage_labs'),
    path('update_labs/<int:id>', views.update_labs, name='update_labs'),
    path('update_labs_status/<int:id>', views.update_labs_status, name='update_labs_status'),
    path('delete_labs/<int:id>', views.delete_labs, name='delete_labs'),

    # Manage sports infrastructure
    path('manage_sports/', views.manage_sports, name='manage_sports'),
    path('update_sports/<int:id>', views.update_sports, name='update_sports'),
    path('update_sports_status/<int:id>', views.update_sports_status, name='update_sports_status'),
    path('delete_sports/<int:id>', views.delete_sports, name='delete_sports'),
]