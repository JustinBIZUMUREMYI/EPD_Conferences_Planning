from django.shortcuts import render, redirect
from .forms import register
from .models import Attendees

def index(request):
    return render(request, 'conference_planning/index.html')


def agenda(request):
    return render(request, 'conference_planning/schedule.html')


def speakers(request):
    return render(request, 'conference_planning/speakers.html')


def sponsors(request):
    return render(request, 'conference_planning/sponsors.html')


def exhibition(request):
    return render(request, 'conference_planning/exhibition.html')


def local_registration(request):
    return render(request, 'conference_planning/registration/registration_local.html')


def international_registration(request):
    return render(request, 'conference_planning/registration/registration_international.html')


def students_registration(request):
    return render(request, 'conference_planning/registration/registration_students.html')


def register(request):
    if request.method == 'POST':
        form = register(request.POST)
        if form.is_valid():
            attendee = Attendees(
                name=form.cleaned_data['name'],
                identity=form.cleaned_data['identity'],
                email=form.cleaned_data['email'],
                country_code=form.cleaned_data['countryCode'],
                phone=form.cleaned_data['phone'],
                country=form.cleaned_data['country'],
                organization=form.cleaned_data['company']
            )
            attendee.save()
            return redirect('index')
    else:
        form = register()
    return render(request, 'registration.html', {'form': form})