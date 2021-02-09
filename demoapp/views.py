from django.shortcuts import render,redirect
from demoapp.models import Student
from demoapp.forms import StudentForm,LoginForm
import random
from django.core.mail import send_mail
from django.conf import settings
from demo.settings import EMAIL_HOST_USER 
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    # otp=str(random.randint(100000,999999))
    sent=False
    if request.method=='POST':
        otp=str(random.randint(100000,999999))
        request.session['otp']=otp
        form=StudentForm(request.POST)
        print(form)
        if form.is_valid():
            cd=form.cleaned_data
            email=cd['emailid']
            form.save()
            # print(otp)
            subject = "OTP"
            message = "Hiiiiiiiiii Satish And Bhanu"+otp
            send_mail(subject,message,EMAIL_HOST_USER,[email])
            sent=True
            return redirect('/')
    
    form=StudentForm()
    return render(request,'demoappt/register.html',{'form':form,'sent':sent})

def login(request):
    if request.user.is_authenticated:
        return render(request, 'demoappt/home.html')
    else:
        return render(request,'demoappt/login.html') 

def dashborad(request):
    if request.method == 'POST':
        if Student.objects.filter(emailid=request.POST['email']).exists():
            student = Student.objects.get(emailid=request.POST['email'])
            return render(request, 'demoappt/home.html', {'student': student})
        else:
            context = {'msg': 'Invalid username or password'}
            return render(request, 'demoappt/login.html', context)
    else:
        return render(request,'demoappt/home.html') 

def logout_view(request):
    # auth.logout(request)
    return redirect(login)