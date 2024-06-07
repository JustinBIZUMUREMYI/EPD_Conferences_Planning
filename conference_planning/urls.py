
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path, include
from . import views

registration_patterns = [
    path('local/', views.local_registration, name='local_registration'),
    path('international/', views.international_registration, name='international_registration'),
    path('students/', views.students_registration, name='students_registration'),
]

admin_urls = [
    path('dashboard', views.dashboard, name="dashboard"),
    path('attendees', views.attendees, name="attendees"),
]

urlpatterns = [
    path('', views.index, name='index'),
    path('agenda/', views.agenda, name='agenda'),
    path('speakers/', views.speakers, name='speakers'),
    path('sponsors/', views.sponsors, name='sponsors'),
    path('registration/', include((registration_patterns, 'registration'), namespace='registration')),   
    path('register/', views.register, name='register'),
    path('auth/', views.login_view, name="login"),
    path('authenticate', views.auth, name="authenticate"),
    path('administration/', include((admin_urls, 'admin'), namespace='admin')),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
