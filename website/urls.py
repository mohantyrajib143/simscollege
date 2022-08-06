from django.contrib import admin
from django.urls import path, include
from website import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('whyus/', views.whyus, name='whyus'),
    path('awards/', views.awards, name='awards'),
    path('science/', views.science, name='science'),
    path('commerce/', views.commerce, name='commerce'),
    path('faculties/', views.faculties, name='faculties'),
    path('entrance/', views.entrance, name='entrance'),
    path('chse/', views.chse, name='chse'),
    path('college/', views.college, name='college'),
    path('hostel/', views.hostel, name='hostel'),
    path('gallery/', views.gallery, name='gallery'),
    path('lab/', views.lab, name='lab'),
    path('sports/', views.sports, name='sports'),
    path('yoga/', views.yoga, name='yoga'),
    path('neet/', views.neet, name='neet'),
    path('iit/', views.iit, name='iit'),
    path('chse_result/', views.chse_result, name='chse_result'),
    path('news/', views.news, name='news'),
    path('notices/', views.notices, name='notices'),
    path('admission/', views.admission, name='admission'),
]