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
def new_dog(request):
    data = request.body
    data = str(data, 'utf-8')
    form = json.loads(data)
    
    dog_name = form.get('dog_name').title()
    age = form.get('age')
    sex = form.get('sex')
    size = form.get('size')
    temperment = form.get('temperment') 
    crate_trained = bool(form.get('crate_trained'))
    details = form.get('details')
    user_profile = UserProfile.objects.get_or_create(user = request.user)[0]
    
    if not age.isdigit() or sex not in 'MF' or size not in 'SML':
        return JsonResponse({'message':'Invalid Input'})

    added = Dog.objects.filter(dog_name = dog_name).exists()


    if added:
        return update_dog(request)

    new_pupp =  Dog(owner = user_profile,dog_name=dog_name, age=age, sex = sex, size=size, temperment = temperment,
    crate_trained = crate_trained,details= details)

    new_pupp.save()
    
    
    return JsonResponse({'message':'New Dog Added'})



# Updating the User Profile


@login_required
def update_user(request):
    data = request.body
    data = str(data, 'utf-8')
    form = json.loads(data)

    user = request.user
    phone_number = form.get('phone_number')
    first_name= form.get('first_name')
    last_name= form.get('last_name')
    address= form.get('address')
    city= form.get('city')
    zipcode= form.get('zipcode')
    share_pupps = form.get('share_pupps')

    user_profile = UserProfile.objects.get_or_create(user=user)[0]
    updated_user = UserProfile.objects.filter(user_profile).update(user=user, phone_number=phone_number, first_name=first_name, last_name=last_name,
    address=address, city=city, zipcode=zipcode, share_pupps=share_pupps)
    update_user.save()    

    return JsonResponse({'message':'User Profile Updated!'})

@login_required
def update_dog(request):
    data = request.body
    data = str(data, 'utf-8')
    form = json.loads(data)



    dog_name = form.get('dog_name').title
    age = form.get('age')
    sex = form.get('sex')
    size = form.get('size')
    temperment = form.get('temperment') 
    crate_trained = form.get('crate_trained')
    details = form.get('details')
    
    user_profile = UserProfile.objects.get_or_create(user=request.user)[0]
    doggie = Dog.objects.filter(dog_name=dog_name).update(owner = user_profile, age =age, sex=sex, size=size, temperment= temperment,
    crate_trained=crate_trained, details = details)


    return JsonResponse({'message': f'{dog_name} Updated!'})