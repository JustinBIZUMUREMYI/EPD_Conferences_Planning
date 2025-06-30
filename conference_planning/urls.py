
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings


registration_patterns = [
    path('attendees/', views.local_registration, name='attendees_registeration'),
    # path('international/', views.international_registration, name='international_registration'),
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
    path('export_locals/', views.export_locals_to_excel, name='export_locals_to_excel'),
    path('export_internationals/', views.export_internationals_to_excel, name='export_internationals_to_excel'),
    path('export_speakers/', views.export_speakers_to_excel, name='export_speakers_to_excel'),
    path('export_panelists/', views.export_panelists_to_excel, name='export_panelists_to_excel'),
    path('export_applicants/', views.export_applicants_to_excel, name='export_applicants_to_excel'),
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
    path('internship', views.interns, name='interns'),

    # medias upload
    path('videos', views.videos.as_view(), name = 'video'),
    path('photos', views.photos.as_view(), name = 'photo'),
    path('internship', views.Register_Interns.as_view(), name = 'internship_Application'),



]

urlpatterns = [
    path('', views.index, name='index'),
    path('videos/', views.previous_videos, name = 'videos'),
    path('photos/', views.previous_photos, name = 'photos'),
    path('Internship_Application/', views.interns_list.as_view(), name = 'internship_Application'),
    path('Submit_application/', views.submit_application.as_view(), name = 'submit_application'),
    path('agenda/', views.agenda, name='agenda'),
    path('speakers/', views.speakers, name='speakers'),
    path('speakers_details/<int:speaker_id>', views.speakers_details, name='speaker_details'),
    path('panelist_details/<int:panelist_id>', views.panelist_details, name='panelist_details'),
    path('sponsors/', views.sponsors, name='sponsors'),
    path('partners/', views.official_partners, name = 'partners'),
    path('sponsorships/', views.sponsorship_packages, name = 'sponsorships'),
    path('exhbitions/', views.exhbition, name = 'exhbition'),
    path('csr/', views.csr, name = 'csr'),
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
