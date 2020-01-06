from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import student 
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.views.generic import View
# Create your views here.

def home(request):
    return render(request,"home.html")

def login(request):
    if request.method=="POST":
        
        global username
        username=request.POST['s1']
        password=request.POST['s2']
        
        user=auth.authenticate(username=username,password=password)
        
        if user is not None:
            auth.login(request,user)
            return redirect("/home")
        
        else:
            messages.info(request,"Invalid Username/Password")
            return redirect("/login")
        

    else:    
        return render(request,"login.html")
def logout(request):
    auth.logout(request)
    return redirect("/home")
    


def signup(request):
    if request.method=="POST":
        sname=request.POST['n1']
        slname=request.POST['n2']        
        semail=request.POST['n4']
        susername=request.POST['u1']
        spassword=request.POST['p1']
        smobile=request.POST['n3']
        sgender=request.POST['n10']
        sdob=request.POST['n5']
        squalification=request.POST['n6']
        saddress=request.POST['n7']
        scountry=request.POST['c1']
        
        if request.POST['p1']==request.POST['p2']:
            if User.objects.all().filter(email=semail).exists():
                messages.info(request,"Email already Taken")
                return redirect("/signup")
            elif User.objects.filter(username=susername).exists():
                messages.info(request,"Username already Taken")
                return redirect("/signup")
            else:
                user=User.objects.create_user(username=susername,email=semail,password=spassword,first_name=sname,last_name=slname)
                user.save()
                s=student.objects.create(sname=sname,slname=slname,scountry=scountry,semail=semail,susername=susername,spassword=spassword,snumber=smobile,sgender=sgender,sdob=sdob,squalification=squalification,sadress=saddress)
                s.save()
                return HttpResponse("<h1>Registerd Succesfully</h1><br><a href='/login'><h2>back to login</h2></a>")

                  
        else:
            messages.info(request,"Password didnt Match")
            return redirect("/signup")
    else:
        return render(request,"signup.html")
def viewdata(request):
    x=username
    
    z=student.objects.all().filter(susername=x)
    return render(request,"viewdata.html",{"z":z})
def update(request):
    if request.method=="POST":
        uname=request.POST['u1']
        udata=request.POST['u2']
        if uname=='FirstName':
            k=student.objects.all().filter(susername=username).update(sname=udata)
            return HttpResponse("<h2>Your Data Is Updated Please Check Your<a href='/viewdata'>updatedData</a>")
        elif uname=='SecondName':
            k=student.objects.all().filter(susername=username).update(slname=udata)
            return HttpResponse("<h2>Your Data Is Updated Please Check Your<a href='/viewdata'>updatedData</a>")
        elif uname=='Email':
            k=student.objects.all().filter(susername=username).update(semail=udata)
            return HttpResponse("<h2>Your Data Is Updated Please Check Your<a href='/viewdata'>updatedData</a>")
        
        elif uname=='MobileNumber':
            k=student.objects.all().filter(susername=username).update(snumber=udata)
            return HttpResponse("<h2>Your Data Is Updated Please Check Your<a href='/viewdata'>updatedData</a>")
        elif uname=='Gender':
            k=student.objects.all().filter(susername=username).update(sgender=udata)
            return HttpResponse("<h2>Your Data Is Updated Please Check Your<a href='/viewdata'>updatedData</a>")
        elif uname=='address':
            k=student.objects.all().filter(susername=username).update(sadress=udata)
            return HttpResponse("<h2>Your Data Is Updated Please Check Your<a href='/viewdata'>updatedData</a>")
        elif uname=='DateofBirth':
            k=student.objects.all().filter(susername=username).update(sdob=udata)
            return HttpResponse("<h2>Your Data Is Updated Please Check Your<a href='/viewdata'>updatedData</a>")
        elif uname=='Qualification':
            k=student.objects.all().filter(susername=username).update(squalification=udata)
            return HttpResponse("<h2>Your Data Is Updated Please Check Your<a href='/viewdata'>updatedData</a>")
        else:
            return redirect("/")
    else:
        return render(request,"update.html")
    
    
    
        
        
    
