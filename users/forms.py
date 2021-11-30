from django import forms
from .models import Profile
from django.contrib.auth.models import User


# to update username and email
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField() #addintionall field
   
    class Meta:
        model = User
        fields = ['username', 'email']
    
# update user profile
# to update profile image 
class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['image', 'about_me', #'product',
                     #'country', 'address'
                ]

