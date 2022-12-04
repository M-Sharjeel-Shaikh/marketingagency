from django.http import HttpResponseNotFound
from django.shortcuts import redirect, render
from clients.models import Clients
from subscriber.models import Subscriber
from django.shortcuts import HttpResponse
from django.contrib import messages

def home(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def client(request):
    return render(request, "client.html")

def contact(request):
    return render(request, "contact.html")

def team(request):
    return render(request, "team.html")

def service(request):
    return render(request, "service.html")

def header(request):
    return render(request, "index.html")

def footer(request):    
    return render(request, "index.html")

def subscriber(request):
    if request.method == "POST":
        email = request.POST['sub_email']
        try:
            if Subscriber.objects.filter( Email = email ).first():
                messages.info(request, "'You have alreday our subscriber' ")
                return redirect('/contact')

            subcriber = Subscriber.objects.create( Email = email )        
            subcriber.save()
            messages.info(request, "'Thanks For Subcriber Us \n'  'You will be updated with our new sevices and offers' ")
            return redirect('/contact')
            
        except Exception as e:
            print(e)
            return HttpResponseNotFound(404)

    return render(request, "index.html")
    

def send(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['contact_no']
        msg = request.POST['message']

        try:
            client = Clients.objects.create(
            Full_Name = name, 
            Phone = phone,
            Email = email,
            Text_area = msg 
            )        
            client.save()
            messages.success(request, 'Your message is received to our team and we will contact back you soon')
            return redirect('/contact')
        except Exception as e:
            print(e)
            return HttpResponse(404)

    return render(request, "contact.html")





