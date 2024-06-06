from django import forms

class register(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    identity = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    countryCode = forms.CharField(max_length=10, required=True)
    phone = forms.CharField(max_length=20, required=True)
    country = forms.CharField(max_length=100, required=True)
    company = forms.CharField(max_length=100, required=False)
    agree_term = forms.BooleanField(required=True, initial=True)