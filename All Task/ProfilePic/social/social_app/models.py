from django.db import models
from django.contrib.auth.models import AbstractUser



class CustomUser(AbstractUser):
    #email = models.EmailField()
    phone_no = models.CharField(max_length=10, blank=True)
    address = models.TextField(blank=True)
    city = models.CharField(max_length=50, blank=True)
    state = models.CharField(max_length=50, blank=True)
    country = models.CharField(max_length=50, blank=True)
    profile_pic = models.ImageField(default='User_Account.png')

    

    

