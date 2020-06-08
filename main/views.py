from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import contactdetails,email_contact
from django.core.mail import send_mail
from django.conf import  settings
from datetime import datetime

# Create your views here.
def homepage(request):
    if request.method=='POST':
            name=request.POST['name1']
            phone=request.POST['phone']
            subject=request.POST['select']
            con=contactdetails(name=name,phone=phone,subjects=subject,time=datetime.now())
            con.save()
            send_mail(subject,name + ' ' +phone+' '+subject,settings.EMAIL_HOST_USER,['faisalsiddique707@gmail.com'],fail_silently=False)
    return render(request,"main/index.html")
def services(request):
    if request.method=='POST':    
        name=request.POST['name1']
        phone=request.POST['phone']
        subject=request.POST['select']
        con=contactdetails(name=name,phone=phone,subjects=subject,time=datetime.now())
        con.save()
        send_mail(subject,name+' '+phone+' '+subject,settings.EMAIL_HOST_USER,['faisalsiddique707@gmail.com'],fail_silently=False)
    return render(request,"main/services.html")
def contact(request):
    if request.method=='POST':
            message=request.POST['message']
            name=request.POST['name']
            subject=request.POST['subject']
            email=request.POST['email']
            econ=email_contact(name=name,email=email,subject=subject,message=message,date=datetime.now())
            econ.save()
            send_mail(subject,name + ' ' + message +' '+ email,settings.EMAIL_HOST_USER,['faisalsiddique707@gmail.com'],fail_silently=False)
    return render(request,"main/contact.html")


def about(request):
    if request.method=='POST':    
        name=request.POST['name1']
        phone=request.POST['phone']
        subject=request.POST['select']
        con=contactdetails(name=name,phone=phone,subjects=subject,time=datetime.now())
        con.save()
        send_mail(subject,name+' '+phone+' '+subject,settings.EMAIL_HOST_USER,['faisalsiddique707@gmail.com'],fail_silently=False)
    return render(request,"main/contact.html")



