from django import forms
from .models import Partner, Sponsor, Speaker, Event, Agenda, Panalist, booth, Testimonial, PreviousVideos, PreviousPhotos, Event, Agenda, Event_days,Sponsorships, Document, BookSponsorship, FloorPlan, BookAccessory,BookBooth 

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

