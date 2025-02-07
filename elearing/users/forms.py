from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Student

class StudentRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    date_of_birth = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    phone_number = forms.CharField(required=False)
    profile_picture = forms.ImageField(required=False)
    bio = forms.CharField(required=False, widget=forms.Textarea)

    class Meta:
        model = Student
        fields = ['username', 'email', 'date_of_birth','phone_number','profile_picture', 'bio']
