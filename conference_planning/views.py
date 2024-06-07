
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import registerForm, LoginForm
from django.contrib import messages
from .models import Attendees
from django.urls import reverse

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
    message = request.GET.get('message', None)
    context = {}
    if message:
        context['message'] = message
    return render(request, 'conference_planning/registration/registration_international.html', context)


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
            success_message = 'Successfully registered. You will receive an email with more details about the event.'
            redirect_url = request.META.get('HTTP_REFERER', '/') + '?message=' + success_message
            return redirect(redirect_url)
        else:
            return_url = request.META.get('HTTP_REFERER', '/')
            return render(request, 'conference_planning/registration/registration_international.html', {'form': form})
    else:
        form = registerForm()
    
    return render(request, 'conference_planning/registration/registration_international.html', {'form': form})


def login_view(request):
    return render(request, 'conference_planning/administration/login.html')


def auth(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('admin:dashboard')
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = LoginForm()
    return render(request, 'conference_planning/administration/login.html', {'form': form})


@login_required
def dashboard(request):
    return render(request, 'conference_planning/administration/index.html')


@login_required
def attendees(request):
    attendees_list = Attendees.objects.all()
    context = {'attendees': attendees_list}
    
    return render(request, 'conference_planning/administration/attends.html', context)