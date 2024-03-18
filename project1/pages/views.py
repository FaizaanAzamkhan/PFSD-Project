from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User

from .models import Register,RoomAllocation


def home(request):
    return render(request,"home.html")

def aboutus(request):
    return render(request,"aboutus.html")

def register(request):
    if request.method == 'POST':
        if request.POST.get('fn') and request.POST.get('ln') and request.POST.get('mb') and request.POST.get('em') and request.POST.get('pwd') and request.POST.get('dob'):
            post = Register()
            post.First_Name = request.POST.get('fn')
            post.Last_Name = request.POST.get('ln')
            post.Mobile = request.POST.get('mb')
            post.Email = request.POST.get('em')
            post.Password = request.POST.get('pwd')
            post.DOB = request.POST.get('dob')
            post.save()

            return render(request, 'register.html')

    else:
        return render(request, 'register.html')

def login(request):
    return render(request,"login.html")

def intro(request):
    return render(request,"navbar.html")

def emptyroom(request):
    return render(request,"emptyroom.html")

def services(request):
    return render(request,"services.html")

def RR(request):
    if request.method == 'POST':
        if request.POST.get('fn') and request.POST.get('ln') and request.POST.get('mb') and request.POST.get('em') and request.POST.get('pwd') and request.POST.get('dob'):
            #
            First_Name = request.POST.get('fn')
            Last_Name = request.POST.get('ln')
            Mobile = request.POST.get('mb')
            Email = request.POST.get('em')
            Password = request.POST.get('pwd')
            DOB = request.POST.get('dob')
            post = RoomAllocation.objects.create(Room_Type=First_Name,AC_NON_AC=Last_Name,Mobile=Mobile,Email=Email,Password=Password,DOB=DOB)
            post.save()
            return render(request, 'RR.html')

    else:
        return HttpResponse('Not a post method....!')




def facilities(request):
    return render(request,"facilities.html")

