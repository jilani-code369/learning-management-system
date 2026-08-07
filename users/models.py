from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    GENDER_CHOICES = (
        ("male","MALE"),
        ("female","FEMALE"),
        ("other", "OTHER"),
        ("prefer not to say", "PREFER NOT TO SAY")
    )
    
    phone = models.CharField(max_length=20, null = True, blank=True)
    address = models.CharField(max_length=200, null = True, blank=True)
    photo = models.ImageField(upload_to='photo/', null = True, blank=True)
    dob = models.DateField( null = True, blank=True)
    gender = models.CharField(max_length=50, choices = GENDER_CHOICES, default = "prefer not to say")

