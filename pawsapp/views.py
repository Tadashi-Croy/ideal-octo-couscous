from django.http.response import HttpResponseRedirect
from django.shortcuts import render, reverse
from django.http import HttpResponse
from .models import Appointment
from django.utils import timezone
from django.utils.timezone import is_aware, make_aware
from datetime import datetime, time
from django.core.mail import send_mail


# Create your views here.

def index(request):



    return render(request, 'pawsapp/index.html')
    

def get_deets(request):
    
    if request.POST:
        form = request.POST
        owner = form['first_name'] + " " + form['last_name']


        if not form.get('first_name') or not form.get('email') or not form.get('phone'):

            return render(request, 'pawsapp/customer_form.html', {'info': 'Please Enter Information Into All Required Fields.'})
            




       
        owner = owner
        email = form['email']
        address = form['address']
        city = form['city']
        phone = form['phone']
        puppy_training = bool(form.get('puppy_training'))
        adolescent_training = bool(form.get('adolescent_training'))
        adult_training = bool(form.get('adult_training'))
        dog_name = form['dog_name']
        dog_detail = form["dog_detail"]
        heard_about = form.get('heard_about',None)
        adoption = form.get('referred',None)
        other = form.get('other',None)
        referred = 'None'

        time1 = form.get('time1')
        time2 = form.get('time2')
        time3 = form.get('time3')
        error_message = None

        if time1:
            try:
                time1 = datetime.strptime(time1,'%Y-%m-%dT%H:%M' ) 
                time1_aware = make_aware(time1)


            except:
                error_message='Please Select a Time'
                time1 = None
        
        else:
            error_message= 'Please Select a Time'
            time1 = None


        if time2:
            try:
                time2 = datetime.strptime(time2,'%Y-%m-%dT%H:%M' )
                time2_aware = make_aware(time2)

            except ValueError:
                error_message = 'Invalid Input'
                time2 = None

        else:
            time2 = None

        
        
        if time3:
        
            try:
                time3 = datetime.strptime(time3,'%Y-%m-%dT%H:%M' )
                time3_aware = make_aware(time3)

            except ValueError:
                time3 = None
                
        else:
            time3 = None

        
        if time1:

            if time1 < datetime.now():
                
                return render(request, 'pawsapp/customer_form.html', {'info': 'Please Enter a Time in the future.'})









        heard_about = 'None Selected'

        if heard_about != 'Other' and heard_about != 'Referral' and heard_about != None:
            referred = heard_about
        elif adoption:
            referred = adoption
        elif other:
            referred = other
        else:
            referred = 'None Selected'


        customer = Appointment(
            owner = owner,
            email = email,
            address = address,
            city = city,
            phone = phone,
            dog_name= dog_name,
            puppy_training = puppy_training,
            adolescent_training = adolescent_training,
            adult_training =adult_training,
            dog_detail =dog_detail,
            heard_about = referred,
            req_appt1 = time1_aware,
            req_appt2 = time2,
            req_appt3 = time3,
        )

        customer.save()
        send_mail(
                    'Appointment Created!',
                    f'Person: {owner} \n {email} \nDog: {dog_name} \nTime Created: {datetime.now()} \nDetails: {dog_detail}\nSee the ADMIN Panel for more information',
                    'from@yourdjangoapp.com',
                    ['tadashicroy@gmail.com'],
                    fail_silently=False,
                )

        context = { 
            'dog_name': form['dog_name'],
            'info': error_message,


            }
        
        return render(request, 'pawsapp/customer_form.html', context)

    else:
        form =''

    return render(request, 'pawsapp/customer_form.html') 


def references(request):


    return render(request, 'pawsapp/references_page.html')