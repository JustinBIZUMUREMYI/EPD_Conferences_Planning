from django.db import models

class Attendees(models.Model):
    class AttendeeType(models.TextChoices):
        LOCAL = "Local", "Local"
        INTERNATIONAL = "International", "International"
        STUDENT = "Student", "Student"

    STATUS_CHOICES = [
        ('organizer', 'Organizer'),
        ('delegate', 'Delegate'),
        ('exhibitor', 'Exhibitor'),
        ('student', 'Student'),
        ('media', 'Media')

       
    ]
    
    
    names = models.CharField(max_length=250)
    email = models.EmailField()
    identity = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    country = models.CharField(max_length=100)
    organization = models.CharField(max_length=100, null=True, blank=True)
    university = models.CharField(max_length=100, null=True, blank=True)
    student_number = models.CharField(max_length=50, null=True, blank=True)
    category = models.CharField(max_length=100, choices=STATUS_CHOICES, default='choose your category')   
    attendee_type = models.CharField(max_length=30, choices=AttendeeType.choices, default=AttendeeType.LOCAL, unique=False)
    registered_on = models.DateTimeField(auto_now_add=True)
    STATUS_CHOICES = [
        ('unpaid', 'Unpaid'),
        ('paid', 'Paid'),
       
    ]
    
    status = models.CharField(
        max_length=100,
        choices=STATUS_CHOICES,
        default='unpaid',
    )
    
    
    class Meta:
        verbose_name_plural = 'Attendees'
        
    def __str__(self) -> str:
        return self.names

class Partner(models.Model):
    organization_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    logo = models.ImageField(upload_to='images/')
    summary = models.TextField(max_length=5000)
    url = models.CharField(max_length=100) 
    
    def __str__(self) -> str:
        return self.organization_name
        
    def get_absolute_url(self):
        return reverse("partner-detail", kwargs={"pk": self.pk})


# class Amount(models.Model):
#     amount = models.CharField(max_length=100)


#     def __str__(self):
#         return self.amount


class Sponsorships(models.Model):
    kind = models.CharField(max_length=100)
    payment = models.CharField(max_length=100)
    benefits = models.TextField(max_length=100000)
   

    def __str__(self) -> str:
        return self.kind


class Sponsor(models.Model):
    sponsorship = models.ForeignKey(Sponsorships, on_delete=models.CASCADE, default='')
    organization_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    logo = models.ImageField(upload_to='images/')
    summary = models.TextField(max_length=5000)
    url = models.CharField(max_length=100) 
    
    def __str__(self) -> str:
        return self.organization_name


class Panalist(models.Model):
    names = models.CharField(max_length=200)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    title = models.CharField(max_length=100)
    bio = models.TextField(max_length=10000)
    picture = models.ImageField(upload_to='images/')

    def __str__(self) -> str:
        return self.names
    
class Speaker(models.Model):
    names = models.CharField(max_length=200)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    title = models.CharField(max_length=100)
    bio = models.TextField(max_length=10000)
    picture = models.ImageField(upload_to='images/')

    def __str__(self) -> str:
        return self.names
    
class Event(models.Model):
    event_title = models.CharField(max_length=300)
    description = models.TextField(max_length=5000)
    organizer = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self) -> str:
        return self.event_title
    
class Event_days(models.Model):
    day_name = models.CharField(max_length=100)
    day_date = models.DateField()
    
    class Meta:
        verbose_name_plural = 'Event_days'

    def __str__(self) -> str:
        return self.day_name

class Agenda(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    day_event= models.ForeignKey(Event_days, on_delete=models.CASCADE, default='')
    activity = models.CharField(default='',max_length=10000)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    class Meta:
        verbose_name_plural = 'Agenda'

    def __str__(self) -> str:
        return self.event
    



class Testimonial(models.Model):
    names = models.CharField(max_length=200)
    title = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='images/')
    testimony = models.TextField(max_length=10000)

    def __str__(self) -> str:
        return self.names

class booth(models.Model):
    name = models.CharField(max_length=200)
    size = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='images/')
    description = models.TextField(max_length=10000)
    amount = models.CharField(max_length=1000)
    booth_number= models.IntegerField(default= '')

    def __str__(self) -> str:
        return self.name
    
class accessory(models.Model):
    name = models.CharField(max_length=400)
    quantity = models.IntegerField()
    picture = models.ImageField(upload_to='images/')
    description = models.TextField(max_length=10000)
    amount = models.CharField(max_length=1000)


    def __str__(self) -> str:
        return self.name


class PreviousVideos(models.Model):
    title = models.CharField(max_length=400)
    video_file = models.FileField(upload_to='videos/')
    conference_year = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.title
    
class PreviousPhotos(models.Model):
    title = models.CharField(max_length=400)
    photo_file = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title


class Document(models.Model):
    title = models.CharField(max_length=1000)
    pdf_document= models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True, )
    
    def __str__(self):
        return self.title





class BookSponsorship(models.Model):
    sponsor_name = models.CharField(max_length = 100)
    company = models.CharField(max_length=100, default = '')
    email = models.EmailField()
    phone_number = models.CharField(max_length=100, default = '')
    sponsorship_package = models.ForeignKey(Sponsorships, on_delete=models.CASCADE, default='')
    # amount = models.CharField(max_length=100)
    STATUS_CHOICES = [
        ('registering', 'Registering'),
        ('registered', 'Registered'),
       
    ]
    
    status = models.CharField(
        max_length=100,
        choices=STATUS_CHOICES,
        default='register',
    )


    def __str__(self):
        return self.sponsor_name

class Countdown(models.Model):
    end_time = models.DateTimeField()


class FloorPlan(models.Model):
    title = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='images/')
    date = models.DateField()


    def __str__(self):
        return self.title


class Booth_space(models.Model):
    space_number = models.CharField(max_length=100) 
     
    def __str__(self):
        return self.space_number

class BookBooth(models.Model):
    Exhibitor_name = models.CharField(max_length = 100)
    Company = models.CharField(max_length=100, default = '')
    Email = models.EmailField()
    Phone_number = models.CharField(max_length=100, default = '')
    Booth = models.ForeignKey(booth, on_delete=models.CASCADE, default='')
    Booth_space = models.ForeignKey(Booth_space, on_delete=models.CASCADE, default='')

    STATUS_CHOICES = [
        ('book', 'Book'),
        ('booked', 'Booked'),
       
    ]
    
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='book',
    )

    def __str__(self) -> str:
        return self.Exhibitor_name

    
class BookAccessory(models.Model):
    Exhibitor_name = models.CharField(max_length = 100)
    Company = models.CharField(max_length=100, default = '')
    Email = models.EmailField()
    Phone_number = models.CharField(max_length=100, default = '')
    Accessory = models.ForeignKey(accessory, on_delete=models.CASCADE, default='')
    

    STATUS_CHOICES = [
        ('book', 'Book'),
        ('booked', 'Booked'),
       
    ]
    
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='book',
    )

    def __str__(self) -> str:
        return self.Exhibitor_name



class PreviousConferences(models.Model):
    edition = models.CharField(max_length=1000)
    year  = models.CharField(max_length=100)
    short_description = models.CharField(max_length=5000)


    def __str__(self) -> str:
        return self.edition


# the table for the professional internship 

class Interns(models.Model):
    Host_Company = models.ForeignKey(Testimonial, on_delete=models.CASCADE, default=1)
    STATUS_CHOICES = [
        ('advanced diploma', 'Advanced Diploma'),
        ('bachelor degree', 'Bachelor Degree'),
        ('master degree', 'Master Degree'),
    
    ]
    Full_Name = models.CharField(max_length=250)
    Email = models.EmailField()
    ID_number = models.CharField(max_length=50)
    Phone = models.CharField(max_length=20)
    Country = models.CharField(max_length=100)
    University = models.CharField(max_length=100)
    Education_level = models.CharField(max_length=100, choices=STATUS_CHOICES, default='choose your category') 
    Qualification = models.CharField(max_length=100)  
    Graduation_date = models.DateField()
    Degree = models.FileField(upload_to='uploads/')
    Resume = models.FileField(upload_to='uploads/')
    Other_documents = models.FileField(upload_to='uploads/', blank=True, null=True)
    registered_on = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name_plural = 'Interns'
        
    def __str__(self) -> str:
        return self.Full_Name

    






