from django import forms

class registerForm(forms.Form):
    name = forms.CharField(max_length=200, required=True)
    identity = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    country_code = forms.CharField(max_length=10, required=True)
    phone = forms.CharField(max_length=20, required=True)
    university = forms.CharField(max_length=100, required=False)
    country = forms.CharField(max_length=100, required=True)
    student_number = forms.CharField(max_length=50, required=False)
    organization = forms.CharField(max_length=100, required=False)
    agree_term = forms.BooleanField(required=True, initial=True)
    return_url = forms.CharField(required=True)
    
    def clean_agree_term(self):
        agree_term = self.cleaned_data.get('agree_term')
        if not agree_term:
            raise forms.ValidationError("You need to accept the terms of service.")
        return agree_term
    
    
class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
