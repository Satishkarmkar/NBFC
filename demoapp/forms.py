from django import forms
from demoapp.models import Student
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields='__all__'
        
class LoginForm(forms.ModelForm):
    class Meta:
        model=Student
        fields=['emailid']

class CreateUserForm(UserCreationForm):
    class Meta:
        fileds=['']