from django import forms
from .models import internship_document, Partner, Sponsor, Speaker, Event, Agenda, Panalist, booth, Testimonial, PreviousVideos, PreviousPhotos, Event, Agenda, Event_days,Sponsorships, Document, BookSponsorship, FloorPlan, BookAccessory,BookBooth, Booth_space 
import re
from .models import Attendees, Interns
from django.core.exceptions import ValidationError


class registerForm(forms.Form):
    name = forms.CharField(max_length=200, required=True)
    identity = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    country_code = forms.CharField(max_length=10, required=True)
    phone = forms.CharField(max_length=20, required=True)
    university = forms.CharField(max_length=100, required=False)
    country = forms.CharField(max_length=100, required=True)
    student_number = forms.CharField(max_length=50, required=False)
    category = forms.CharField(max_length=100, required=False)
    organization = forms.CharField(max_length=100, required=False)
    agree_term = forms.BooleanField(required=True, initial=True)
    return_url = forms.CharField(required=True)

    def clean_agree_term(self):
        agree_term = self.cleaned_data.get('agree_term')
        if not agree_term:
            raise forms.ValidationError("You need to accept the terms of conditions to continue.")
        return agree_term
    
    def clean_phone(self):
        phone = self.cleaned_data['phone']
        if not phone.isdigit():
            raise forms.ValidationError("Phone number must contain digits only.")
        if len(phone) < 6 or len(phone) > 15:
            raise forms.ValidationError("Phone number must be between 6 and 15 digits.")
        return phone


    # def clean_identity(self):
    #     identity = self.cleaned_data.get('identity')

    #     # More flexible regex patterns
    #     id_pattern = re.compile(r'^\d{0,16}$')  # IDs between 6 and 12 digits
    #     passport_pattern = re.compile(r'^[A-Z0-9]{8,9}$')  # Passports are 8 to 9 alphanumeric characters

    #     if not (id_pattern.match(identity) or passport_pattern.match(identity)):
    #         raise forms.ValidationError("Invalid ID or Passport number")

    #     return identity
   
    # def clean_phone(self):
    #     phone = self.cleaned_data.get('phone')
    #     if not phone.isdigit():
    #         raise forms.ValidationError('Phone number must contain only digits.')
    #     return phone

    # def clean(self):
    #     cleaned_data = super().clean()
    #     identity = cleaned_data.get('identity')
    #     email = cleaned_data.get('email')
    #     country_code = cleaned_data.get('country_code')
    #     phone = cleaned_data.get('phone')

    #     if country_code and phone:
    #         full_phone = country_code + phone

    #     if Attendees.objects.filter(identity=identity).exists():
    #         raise forms.ValidationError('You are already registered with this identity.')
        
    #     if Attendees.objects.filter(email=email).exists():
    #         raise forms.ValidationError('You are already registered with this email.')

    #     if Attendees.objects.filter(phone=phone).exists():
    #         raise forms.ValidationError('You are already registered with this phone number.')

    #     return cleaned_data
    
    
class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)


class PartnerForm(forms.ModelForm):
    class Meta:
        model = Partner
        fields = "__all__"

class SponsorForm(forms.ModelForm):
    class Meta:
        model = Sponsor
        fields = "__all__"
class SpeakerForm(forms.ModelForm):
    class Meta:
        model = Speaker
        fields = "__all__"
class PanalistForm(forms.ModelForm):
    class Meta:
        model = Panalist
        fields = "__all__"
class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = "__all__"
class boothForm(forms.ModelForm):
    class Meta:
        model = booth
        fields = "__all__"

class VideoForm(forms.ModelForm):
    class Meta:
        model =  PreviousVideos
        fields = '__all__'

class PhotoForm(forms.ModelForm):
    class Meta:
        model =  PreviousPhotos
        fields = '__all__'

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = "__all__"

class AgendaForm(forms.ModelForm):
    class Meta:
        model = Agenda
        fields = "__all__"

class RegisterdayForm(forms.ModelForm):
    class Meta:
        model = Event_days
        fields = "__all__"   

class SponsorshipForm(forms.ModelForm):
    class Meta:
        model = Sponsorships
        fields = '__all__'

class PDFFileForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['title', 'pdf_document']

class FloorplanForm(forms.ModelForm):
    class Meta:
        model = FloorPlan
        fields = ['title', 'picture', 'date']


class BookSponsorshipForm(forms.ModelForm):
    class Meta:
        model = BookSponsorship
        fields = '__all__'
        exclude = ['status']

class BookAccessoryForm(forms.ModelForm):
    class Meta:
        model = BookAccessory
        fields = '__all__'
        exclude = ['status']

class BookBoothForm(forms.ModelForm):
    class Meta:
        model = BookBooth
        fields = '__all__'
        exclude = ['status']


    @staticmethod
    def get_available_booths():
        # Get all booked booth spaces
        booked_booths = BookBooth.objects.values_list('Booth_space', flat=True)
        # Return only the booth spaces that are not booked
        return Booth_space.objects.exclude(id__in=booked_booths)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Define booked_booths within the __init__ method
        booked_booths = BookBooth.objects.values_list('Booth_space', flat=True)
        # Set the queryset for the Booth_space field to only include available booth spaces
        self.fields['Booth_space'].queryset = Booth_space.objects.exclude(id__in=booked_booths)
        # Optional: Disable the dropdown options that are booked, but still show them as disabled
        for choice in self.fields['Booth_space'].choices:
            if choice[0] in booked_booths:
                self.fields['Booth_space'].widget.attrs.update({'disabled': 'disabled'})



class InternsForm(forms.ModelForm):
    class Meta:
        model = Interns
        fields = ['Host_Company','Full_Name','Email','ID_number', 'Phone','Country','University', 'Education_level' , 'Qualification', 'Graduation_date','Degree', 'Resume', 'Other_documents']
    Graduation_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Display only companies with the name 'EPD'
        self.fields['Host_Company'].queryset = internship_document.objects.filter(title__icontains='Position')
    
     # Custom validation for phone number
    def clean_phone(self):
        phone = self.cleaned_data['phone']
        if not phone.isdigit():
            raise forms.ValidationError("Phone number must contain digits only.")
        if len(phone) < 6 or len(phone) > 15:
            raise forms.ValidationError("Phone number must be between 6 and 15 digits.")
        return phone

    # Custom validation for ID number
    def clean_ID_number(self):
        id_number = self.cleaned_data.get('ID_number')
        if id_number:
            if not id_number.isdigit() or len(id_number) != 16:  # Example: Rwanda ID numbers are 16 digits
                raise ValidationError('Enter a valid 16-digit ID number.')
        else:
            raise ValidationError('ID number is required.')
        return id_number
    
    # def clean_Email(self):
    #     email = self.cleaned_data.get('Email')
    #     if Interns.objects.filter(Email=email).exists():
    #         raise forms.ValidationError('An intern with this email already exists.')
    #     return email

    # def clean_ID_number(self):
    #     id_number = self.cleaned_data.get('ID_number')
    #     if Interns.objects.filter(ID_number=id_number).exists():
    #         raise forms.ValidationError('An intern with this ID number already exists.')
    #     return id_number


    