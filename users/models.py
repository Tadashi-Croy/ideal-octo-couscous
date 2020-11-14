from django.db import models
from django.db.models import fields
from django.db.models.base import Model
from django.forms import ModelForm
from django.contrib.auth.models import AbstractUser, User
from django.db.models.deletion import CASCADE
from django.core.exceptions import ValidationError

# Create your models here.
def dog_sizer(size):
    DOG_SIZE = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large')
    )

    if size not in DOG_SIZE:
        raise ValidationError('Invalid Response')


DOG_MF = (
    ('M', 'Male'),
    ('F', 'Female')
)




class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT, related_name='user_profile')
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    first_name= models.CharField(max_length=50, blank=True, null=True)
    last_name= models.CharField(max_length=50, blank=True, null=True)
    address= models.CharField(max_length= 100, blank=True, null=True)
    city= models.CharField(max_length=50, default='Portland')
    zipcode= models.CharField(max_length=10, default='97214')
    share_pupps = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user}' 


class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['phone_number', 'first_name', 'last_name', 'address', 'city', 'zipcode', 'share_pupps']




class Dog(models.Model):

    DOG_SIZE = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large')
    )
    DOG_MF = (
        ('M', 'Male'),
        ('F', 'Female')
    )
    

    owner = models.ForeignKey(UserProfile, on_delete=CASCADE)
    dog_name= models.CharField(max_length=100, blank=True, null=True)
    age= models.IntegerField(default=0, blank=True, null = True)

    sex= models.CharField(max_length=1, choices=DOG_MF)
    size = models.CharField(max_length=1, choices=DOG_SIZE, validators=[dog_sizer])
    
    temperment= models.CharField(max_length=50, blank=True, null=True)
    crate_trained= models.BooleanField(blank=True, null=True)
    
    
    details= models.CharField(max_length=400)


    def __str__(self):
        return self.dog_name


class DogForm(ModelForm):
    class Meta:
        model= Dog
        fields = ['dog_name', 'age', 'sex', 'size', 'temperment', 'crate_trained', 'details']


