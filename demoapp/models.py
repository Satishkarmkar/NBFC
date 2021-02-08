from django.db import models

# Create your models here.
class Student(models.Model):
    fname=models.CharField(max_length=50,verbose_name="Enter Your First Name")
    lname=models.CharField(max_length=50,verbose_name="Enter Your Last Name")
    gender=models.CharField(verbose_name='Choose Your Gender',max_length=10)
    emailid=models.EmailField(max_length=250,verbose_name='Enter Your Email Id')
    phone=models.IntegerField(verbose_name='Enetr Your Mobile Number')
    

