from django import forms

from vendorapp.models import User,Company
from django.contrib.auth.forms import UserCreationForm



class VendorRegistrationForm(UserCreationForm):
    class Meta:
        model=Company
        fields=["company_name","description","address","company_logo","office_location","pin","website","email","phone","address"]

class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)