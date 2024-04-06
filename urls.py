from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('home/', views.home, name='home'),
    path('job-matching/headhunt/', views.job_matching_headhunt, name='job_matching_headhunt'),
    path('job-matching/candidate/', views.job_matching_candidate, name='job_matching_candidate'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('test/', views.index),
    path('add/', views.add_data),
    path('show/', views.get_all_data),
]
