from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from users.models import UserProfile, Dog


# Create your models here.

class Appointment(models.Model):

    owner = models.ForeignKey(User, on_delete=CASCADE)
    req_appt1 = models.DateTimeField( blank=True, null=True )
    req_appt2 = models.DateTimeField( blank=True, null=True)
    req_appt3 = models.DateTimeField( blank=True, null=True)

    appt_dog = models.ForeignKey(Dog, on_delete=CASCADE)

    def __str__(self):
        return  f'{self.owner}: {self.appt_dog}'

