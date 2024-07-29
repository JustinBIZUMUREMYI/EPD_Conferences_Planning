
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings


registration_patterns = [
    path('local/', views.local_registration, name='local_registration'),
    path('international/', views.international_registration, name='international_registration'),
    path('students/', views.students_registration, name='students_registration'),
    path('registration/', views.registration_froms.as_view(), name = 'registration'),
    
]

admin_urls = [
    path('dashboard', views.dashboard, name="dashboard"),
    path('attendees', views.attendees, name="attendees"),
    path('sponsor', views.Register_sponsor.as_view(), name = 'sponsor'),
    path('partner', views.Register_parner.as_view(), name='partner'),
    path('speaker', views.Register_speaker.as_view(), name='speaker'),
    path('panalist', views.Register_panalist.as_view(),name='panalist'),
    path('testimonial', views.Register_testimonial.as_view(), name='testimonial'),
    path('booth', views.Register_booth.as_view(), name='booth'),
    path('event', views.Register_event.as_view(), name = 'event'),
    path('agendas', views.Register_agenda.as_view(), name = 'agendas'),
    path('register_eventday', views.Register_Eventday.as_view(), name = 'dayofevent'),
    path('sponsorships', views.sponsorship.as_view(), name = 'sponsorships'),
    path('export_attendees/', views.export_attendees_to_excel, name='export_attendees_to_excel'),


    # report urls
    path('partners_list', views.partners_list.as_view(), name = 'partners_list'),
    path('sponsors_list', views.sponsors_list.as_view(), name = 'sponsors_list'),
    path('speakers_list', views.speakers_list.as_view(), name = 'speakers_list'),
    path('panalists_list', views.panalists_list.as_view(), name = 'panalists_list'),
    path('testimonials_list', views.testimonials_list.as_view(), name = 'testimonials_list'),
    path('booths_list', views.booths_list.as_view(), name = 'booths_list'),
    path('event_display', views.Display_event.as_view(), name = 'eventDisplay'),
    path('agenda_display', views.Display_agenda.as_view(), name = 'agendaDisplay'),

    # Categories lists
    path('locals', views.locals, name = 'locals'),
    path('internationls', views.internationals, name = 'internationals'),
    path('students', views.students, name = 'students'),

    # medias upload
    path('videos', views.videos.as_view(), name = 'video'),
    path('photos', views.photos.as_view(), name = 'photo'),


]

urlpatterns = [
    path('', views.index, name='index'),
    path('videos/', views.previous_videos, name = 'videos'),
    path('photos/', views.previous_photos, name = 'photos'),
    path('agenda/', views.agenda, name='agenda'),
    path('speakers/', views.speakers, name='speakers'),
    path('sponsors/', views.sponsors, name='sponsors'),
    path('partners/', views.official_partners, name = 'partners'),
    path('sponsorships/', views.sponsorship_packages, name = 'sponsorships'),
    path('exhbitions/', views.exhbition, name = 'exhbition'),
    path('lightinghomes/', views.lighting_homes, name = 'lighting_homes'),
    path('firstedition/', views.First_edition, name='first_edition'),
    path('secondedition/', views.Second_edition, name='second_edition'),
    path('thirdedition/', views.Third_edition, name='third_edition'),
    path('registration/', include((registration_patterns, 'registration'), namespace='registration')),   
    path('register/', views.register, name='register'),
    path('auth/', views.login_view, name="login"),
    path('authenticate', views.auth, name="authenticate"),
    path('administration/', include((admin_urls, 'administration'), namespace='administration')),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
