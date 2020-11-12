from django.contrib import admin
from .models import UserProfile, Dog

# from django.contrib.auth.admin import UserAdmin
# Register your models here.

admin.site.register(UserProfile)
admin.site.register(Dog)