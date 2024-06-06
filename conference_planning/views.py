from django.shortcuts import render

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
