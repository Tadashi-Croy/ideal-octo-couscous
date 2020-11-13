from django.http.response import HttpResponseRedirect
from django.shortcuts import render, reverse
from django.http import HttpResponse


# Create your views here.

def index(request):



    return render(request, 'pawsapp/index.html')
    

def get_deets(request):
    
    if request.POST:
        form = request.POST
        owner = form['first_name'] + " " + form['last_name']
        # customer = Customer(
        #     owner = owner,
        #     phone = form['phone'],
        #     address = form['address'],
        #     city = form['city'],
        #     state = form['state'],
        #     zip_code= form['zip_code'],
        #     email = form['email'],
        # )

        # customer.save()

        # dog_info = Dog_info.objects.all()
        # customer_info = Customer.objects.all()

        # context = { 
        #     'dog_info': dog_info,
        #     'customer_info': customer_info,
        #     'form': form
        #     }
        
        return render(request, 'pawsapp/index.html')
        # return render(request, 'pawsapp/customer_form.html', context)

    else:
        form =''

    print(form)
    return render(request, 'pawsapp/customer_form.html') 


def references(request):


    return render(request, 'pawsapp/references_page.html')