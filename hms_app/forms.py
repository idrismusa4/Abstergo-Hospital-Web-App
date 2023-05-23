from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class patient_registration_form(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ("first_name","last_name","email","username","password1","password2")
    

