from django import forms
from .models import UserProfile

class UserProfilForm(forms.ModelForm):
    model = UserProfile
    fields = ['username','email','age']
    