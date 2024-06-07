from django.shortcuts import render, redirect
from .forms import registerForm
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
        form = registerForm(request.POST)
        if form.is_valid():
            attendee_type = 'LCL'
            stud_number = None
            school = None
            
            if form.cleaned_data['country_code'] != '250':
                attendee_type = 'INTL'
            
            if 'student_number' in form.cleaned_data and form.cleaned_data['student_number']:
                stud_number = form.cleaned_data['student_number']
                attendee_type = 'STUD'
                
            if 'university' in form.cleaned_data and form.cleaned_data['university']:
                school = form.cleaned_data['university']
                attendee_type = 'STUD'
            
            attendee = Attendees(
                names=form.cleaned_data['name'],
                identity=form.cleaned_data['identity'],
                email=form.cleaned_data['email'],
                phone=form.cleaned_data['country_code'] + form.cleaned_data['phone'],
                attendee_type=attendee_type,
                university=school,
                student_number=stud_number,
                country=form.cleaned_data['country'],
                organization=form.cleaned_data['organization']
            )
            attendee.save()
            return redirect('registered')
        else:
            return render(request, 'conference_planning/registration/registration_international.html', {'form': form})
    else:
        form = registerForm()
    
    return render(request, 'conference_planning/registration/registration_international.html', {'form': form})


def registered(request):
    return render(request, 'conference_planning/registered.html')