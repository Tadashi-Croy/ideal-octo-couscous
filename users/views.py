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
            request.session.set_expiry(0)


            return redirect('users:personal_profile')    
        else:
            return render(request, 'users/log_in.html', {'info': 'Incorrect Username or Password'})
            

    return render(request, 'users/log_in.html')

def log_out(request):
    logout(request)

    return redirect('pawsapp:index')

@login_required
def personal_profile(request):
    profile = ''
    user = request.user

    if not UserProfile.objects.filter(user = user):

        return render(request, 'users/personal_profile.html')

    else:

        profile = UserProfile.objects.get(user = user)
        dogs = Dog.objects.filter(owner=profile)

        context = {
            'dogs' : dogs,
            'profile':profile
        }

        return render(request, 'users/personal_profile.html', context)


@login_required
def new_dog(request):

    if request.method == 'GET':
        user = request.user
        dog_dict = {}
        count = 0
        user_profile = UserProfile.objects.get(user=user)
        dogs = Dog.objects.filter(owner=user_profile)

        for dog in dogs:
            add = {
                'name':dog.dog_name,
                'age': dog.age,
                'sex': dog.sex,
                'size': dog.size,
                'temperment': dog.temperment,
                'crate_trained': dog.crate_trained,
                'details': dog.details,
                'id': dog.id                
                }

            dog_dict.update({count:add})
            count += 1
            
        

        return JsonResponse(dog_dict)

    

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
    
    if not age.isdigit() or sex not in 'MF' or size not in 'SML' or dog_name == '':
        return JsonResponse({'message':'Invalid Input'})

    added = Dog.objects.filter(owner = user_profile, dog_name = dog_name).exists()
    added2 = Dog.objects.filter(owner = user_profile, dog_name = dog_name)



    if added:
        return update_dog(request)

    new_pupp =  Dog(owner = user_profile,dog_name=dog_name, age=age, sex = sex, size=size, temperment = temperment,
    crate_trained = crate_trained,details= details)

    new_pupp.save()
    
    
    return JsonResponse({'message':'New Dog Added'})



# NEED USER PROFILE VALIDATION, USE VUE?


@login_required
def update_user(request):

    if request.method == 'GET':
        user = request.user
        user_dict = {}

        profile_exists = UserProfile.objects.filter(user=user).count()

        if profile_exists == 1:

            user_profile = UserProfile.objects.get(user=user)

            
            user_dict = {
                
                'phone_number' : user_profile.phone_number,
                'first_name': user_profile.first_name,
                'last_name': user_profile.last_name,
                'address' : user_profile.address,
                'city' : user_profile.city,
                'zipcode': user_profile.zipcode,
                'share_pupps' : user_profile.share_pupps}            
        
        return JsonResponse(user_dict)

    data = request.body
    data = str(data, 'utf-8')
    form = json.loads(data)
    count = 0
    message = 'User Profile Updated!'
    user = request.user
    user_dict = {
                'phone_number' : form.get('phone_number'),
                'first_name': form.get('first_name'),
                'last_name': form.get('last_name'),
                'address' : form.get('address'),
                'city' : form.get('city'),
                'zipcode': form.get('zipcode'),
                'share_pupps' : form.get('share_pupps')
                }
    user_profile = UserProfile.objects.get_or_create(user=user)[0]

    updated_user = UserProfile.objects.filter(user=user).values()




    for item in updated_user:
        for thing in item:

            if thing in user_dict:
                if not user_dict[thing]:
                    user_dict[thing] = item[thing]

                    count += 1

    if count == 7:
        message = 'No Data Input'    
    

    updated_user = UserProfile.objects.filter(user =user).update(user=user, phone_number=user_dict['phone_number'], first_name=user_dict['first_name'], last_name= user_dict['last_name'],
                    address=user_dict['address'], city=user_dict['city'], zipcode=user_dict['zipcode'], share_pupps= user_dict['share_pupps'])
    
    # updated_user.save()    

    return JsonResponse({'message': message, 'user_info': user_dict })

@login_required
def update_dog(request):
    data = request.body
    data = str(data, 'utf-8')
    form = json.loads(data)



    dog_name = form.get('dog_name').title()
    age = form.get('age')

    if not age.isdigit():
        return JsonResponse({'message': 'Invalid Data Entry'})

    sex = form.get('sex')
    size = form.get('size')
    temperment = form.get('temperment') 
    crate_trained = bool(form.get('crate_trained'))
    details = form.get('details')
    
    user_profile = UserProfile.objects.get_or_create(user=request.user)[0]


    doggie = Dog.objects.filter(dog_name=dog_name).update(owner = user_profile, age =age, sex=sex, size=size, temperment= temperment,
    crate_trained=crate_trained, details = details)

    if doggie == 0:
        new_dog(request)




    return JsonResponse({'message': f'{dog_name} Updated!'})



@login_required
def dog_deleter(request):
    data = request.body
    data = str(data, 'utf-8')
    form = json.loads(data)
    i = form.get('dog_delete')
    to_destroy = Dog.objects.filter(id = i)
    to_destroy.delete()



    return JsonResponse({'message': 'Dog Removed!'})