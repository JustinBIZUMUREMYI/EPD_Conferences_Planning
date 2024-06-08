from django.db import models

class Attendees(models.Model):
    class AttendeeType(models.TextChoices):
        LOCAL = "Local", "Local"
        INTERNATIONAL = "International", "International"
        STUDENT = "Student", "Student"
        
    names = models.CharField(max_length=250)
    email = models.EmailField()
    identity = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    country = models.CharField(max_length=100)
    organization = models.CharField(max_length=100, null=True, blank=True)
    university = models.CharField(max_length=100, null=True, blank=True)
    student_number = models.CharField(max_length=50, null=True, blank=True)
    attendee_type = models.CharField(max_length=30, choices=AttendeeType.choices, default=AttendeeType.LOCAL, unique=False)
    registered_on = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'Attendees'
        
    def __str__(self) -> str:
        return self.names

class Sponsor(models.Model):
    organization = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    logo = models.ImageField(upload_to='images/')
    summary = models.TextField(max_length=5000)
    url = models.CharField(max_length=100) 
    
class Speaker(models.Model):
    names = models.CharField(max_length=200)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    title = models.CharField(max_length=100)
    bio = models.TextField(max_length=10000)
    picture = models.ImageField(upload_to='images/')
    
class Event(models.Model):
    event_title = models.CharField(max_length=300)
    description = models.TextField(max_length=5000)
    organizer = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    
class Agenda(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    
class Testimonial(models.Model):
    names = models.CharField(max_length=200)
    title = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='images/')
    testimony = models.TextField(max_length=1000)