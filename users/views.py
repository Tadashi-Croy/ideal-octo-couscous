from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth  import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import UserProfile, UserProfileForm, DogForm, Dog
import json


# Create your views here.


def index(request):
    

    return render(request, 'users/index.html')

def sign_up(request):
    
    if request.POST:
        print(request.POST)
        form = request.POST
        username = form.get('username')
        password = form.get('password')
        re_pass = form.get('re-password')
        email= form.get('email')
        re_email = form.get('re-email') 

        for item in form:
            error = form[item]
            
            if error == '':
                return render(request, 'users/sign_up.html', {'error': 'The Entire form must be filled out!' })
            pass

        if password == re_pass and email == re_email:

            print(password, email) 
            taken = User.objects.filter(username=username)
            if taken:
                return render(request, 'users/sign_up.html', {'taken': 'Username is Taken'})
            else:
                user = User.objects.create_user(username= username, password=password, email=email)

                return redirect('users:log_in')

        else:
            return render(request, 'users/sign_up.html', {'taken': 'Password/Email Fields Do Not Match'})


    return render(request, 'users/sign_up.html')

def log_in(request):

    if request.POST:
        form = request.POST
        username =form.get('username')
        password = form.get('password')


        user_auth = authenticate(username=username, password = password)

        if user_auth:
            login(request, user_auth)
            return redirect('users:personal_profile')    

    return render(request, 'users/log_in.html')

def log_out(request):
    logout(request)

    return redirect('pawsapp:index')

@login_required
def personal_profile(request):
    user = request.user

    if not UserProfile.objects.filter(user = user):

        return render(request, 'users/personal_profile.html')

    else:

        profile = UserProfile.objects.get(user = user)
        dogs = Dog.objects.filter(owner=profile)

        context = {
            'dogs' : dogs,
        }

        return render(request, 'users/personal_profile.html', context)


@login_required
def update_dog(request):
    data = request.body
    data = str(data, 'utf-8')
    test = json.loads(data)
    print(test, type(test))
    

    return JsonResponse({'hello':'world'})