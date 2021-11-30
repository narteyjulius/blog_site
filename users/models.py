from django.db import models
from django.contrib.auth.models import User 
from django.urls import reverse
# from django_countries.fields import CountryField



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(max_length=300, null=True, blank=True,
                                    # default='sylarport/default.jpg',
                                    #  upload_to="sylarport",
                                     upload_to="profile_image",  default='media/o.jpg')
    about_me = models.TextField()

    def __str__(self):
        return f'{self.user.username} Profile'


    