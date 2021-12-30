from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class createResume(models.Model):
    name=models.CharField(max_length=122)
    address=models.TextField(max_length=500)
    phone=models.CharField(max_length=12)
    email=models.CharField(max_length=122)
    aboutyou=models.TextField(max_length=1000)
    careerobj=models.TextField(max_length=500)
    ssc=models.CharField(max_length= 10)
    hsc=models.CharField(max_length= 10)
    college=models.CharField(max_length= 100)
    degree=models.CharField(max_length= 100)
    cgpa=models.CharField(max_length= 10)
    comname3=models.CharField(max_length=500,blank=True)
    j3sd=models.DateField(blank=True, null=True)
    j3ed=models.DateField(blank=True, null=True)
    positiondet3=models.TextField(max_length=500)
    comname2=models.CharField(max_length=500,blank=True)
    j2sd=models.DateField(blank=True, null=True)
    j2ed=models.DateField(blank=True, null=True)
    positiondet2=models.TextField(max_length=500)
    comname1=models.CharField(max_length=500,blank=True)
    j1sd=models.DateField(blank=True, null=True) 
    j1ed=models.DateField(blank=True, null=True)
    positiondet1=models.TextField(max_length=500)
    references=models.TextField(max_length=600)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    template=models.CharField(max_length=122)
        
    def __str__(self):
            return self.name
        
class contactus(models.Model):
    fname=models.CharField(null=False, max_length=122)
    contact=models.CharField(blank=True,max_length=15)
    query=models.TextField(max_length=1000)

    def __str__(self):
        return self.fname