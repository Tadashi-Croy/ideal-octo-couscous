from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.utils import timezone
from users.models import UserProfile, Dog


# Create your models here.

class Appointment(models.Model):

    created_at = models.CharField(max_length = 100, default = timezone.now())
    replied_to = models.BooleanField(default=False)
    owner = models.CharField(max_length=100)
    email = models.EmailField(max_length= 50,blank=True, null=True)
    address= models.CharField(max_length= 50, blank=True, null=True)
    city = models.CharField(max_length= 50, blank=True, null=True)
    phone = models.CharField(max_length= 50, blank=True, null=True)
    puppy_training = models.BooleanField(default=False)
    adolescent_training = models.BooleanField(default=False)
    adult_training = models.BooleanField(default=False)
    dog_detail = models.CharField(max_length=500, blank=True, null=True)
    heard_about = models.CharField(max_length=100, default='Google')
    dog_name = models.CharField(max_length=50, blank=True, null=True)
    req_appt1 = models.DateTimeField( blank=True, null=True )
    req_appt2 = models.DateTimeField( blank=True, null=True)
    req_appt3 = models.DateTimeField( blank=True, null=True)

    

    def __str__(self):
        return  f'{self.email}: {self.dog_name}'

