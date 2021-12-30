from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class RegisterForm(models.Model):
    username=models.CharField(max_length=122)
    email=models.EmailField(max_length= 122)
    Password=models.CharField(max_length=16)
    
    def __str__(self):
        return self.username

tchoices=(
    ("Template-1","pt-1.html"),
    ("Template-2","pt-2.html"),
    ("Template-3","pt-3.html"),
)

class Createportfolio(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE, null=False, default=False)
    template_url=models.SlugField(max_length=200,null=False,unique=True, primary_key=True)
    name=models.CharField(max_length=50)
    prof=models.CharField(max_length=100)
    # about_us
    about_info=models.CharField(max_length=1000)
    # projects
    p1_title=models.CharField(max_length=50)
    p1_content=models.CharField(max_length=500)
    p1_url=models.URLField()
    
    p2_title=models.CharField(max_length=50)
    p2_content=models.CharField(max_length=500)
    p2_url=models.URLField()
    
    p3_title=models.CharField(max_length=50)
    p3_content=models.CharField(max_length=500)
    p3_url=models.URLField()
    
    #contact section
    instagram=models.URLField(blank=True)
    github=models.URLField()
    linkedin=models.URLField()
    gmail=models.URLField()
    templates=models.CharField(
        max_length= 122,
        choices=tchoices,
        default=1
    )
    
    def __str__(self):
        return self.template_url