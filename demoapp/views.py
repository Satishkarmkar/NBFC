from django.shortcuts import render,redirect
from demoapp.models import Student
from demoapp.forms import StudentForm,LoginForm
import random

# Create your views here.
def index(request):
    otp=str(random.randint(100000,999999))
    sent=False
    if request.method=='POST':
        form=StudentForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            sent=True
            return redirect('/')
    
    form=StudentForm()
    return render(request,'demoappt/register.html',{'form':form,'otp':otp,'sent':sent})

def login(request):
    fom1=LoginForm()
    print(fom1)
    return render(request,'demoappt/login.html',{'fom1':fom1}) 