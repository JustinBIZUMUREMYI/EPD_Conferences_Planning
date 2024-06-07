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
