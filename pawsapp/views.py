from django.http.response import HttpResponseRedirect
from django.shortcuts import render, reverse
from django.http import HttpResponse
from .models import Appointment
from django.utils import timezone
from django.utils.timezone import make_aware
from datetime import datetime, time


# Create your views here.

def index(request):



    return render(request, 'pawsapp/index.html')
    

def get_deets(request):
    
    if request.POST:
        form = request.POST
        owner = form['first_name'] + " " + form['last_name']

        print(form)
        owner = owner
        email = form['email']
        address = form['address']
        city = form['city']
        phone = form['phone']
        puppy_training = bool(form.get('puppy_training'))
        adolescent_training = bool(form.get('adolescent_training'))
        adult_training = bool(form.get('adult_training'))
        dog_name = form['dog_name']
        dog_detail = form['dog_detail']
        heard_about = form.get('heard_about',None)
        time1 = form['time1']
        time2 = form['time2']
        time3 = form['time3']
        adoption = form.get('referred',None)
        other = form.get('other',None)
        referred = 'None'

        
        print(time1)
        # datetime_object = datetime.strptime(time1, '%Y %m %d %I:%M')
        # 2020-11-16T21:28
        # print(datetime_object)

        if heard_about != 'Other' and heard_about != 'Referral':
            referred = heard_about
        elif adoption:
            referred = adoption
        elif other:
            referred = other
        else:
            referred = 'None Selected'


        # customer = Appointment(
        #     owner = owner,
        #     email = email,
        #     address = address,
        #     city = city,
        #     phone = phone,
        #     dog_name= dog_name,
        #     puppy_training = puppy_training,
        #     adolescent_training = adolescent_training,
        #     adult_training =adult_training,
        #     dog_detail =dog_detail,
        #     heard_about = referred,
        #     req_appt1 = time1,
        #     req_appt2 = time2,
        #     req_appt3 = time3,
        # )

        # customer.save()
        # print(customer)

        context = { 
            'dog_name': form['dog_name'],
            'info': 'Appointment Submitted'

            }
        
        return render(request, 'pawsapp/customer_form.html', context)
        # return render(request, 'pawsapp/customer_form.html', context)

    else:
        form =''

    # print(form)
    return render(request, 'pawsapp/customer_form.html') 


def references(request):


    return render(request, 'pawsapp/references_page.html')