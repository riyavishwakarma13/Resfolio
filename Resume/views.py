from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import contactus, createResume

# Create your views here.

def core(request):
    return render(request,"core.html")

def contact(request):
    if request.method == "POST":
        print("test1222")
        fname=request.POST.get('fname')
        contact=request.POST.get('contact')
        query=request.POST.get('query')
        conwithus=contactus(fname=fname,contact=contact,query=query)
        conwithus.save()
        messages.success(request, "Your Info has been sent")
    return render(request,"contact.html")

@login_required
def choose(request):
    return render(request, "choose.html")

def resume_det(request):
    if request.method == "POST":
        name = request.POST.get('fullname')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        aboutyou = request.POST.get('aboutyou')
        careerobj = request.POST.get('careerobj')
        ssc=request.POST.get('ssc')
        hsc=request.POST.get('hsc')
        college=request.POST.get('college')
        degree=request.POST.get('degree')
        cgpa=request.POST.get('cgpa')
        comname3=request.POST.get('comname3')
        j3sd = request.POST.get('j3sd')
        j3ed = request.POST.get('j3ed')
        positiondet3 = request.POST.get('positiondet3')
        comname2=request.POST.get('comname2')
        j2sd = request.POST.get('j3sd')
        j2ed = request.POST.get('j3ed')
        positiondet2 = request.POST.get('positiondet2')
        comname1=request.POST.get('comname1')
        j1sd = request.POST.get('j1sd')
        j1ed = request.POST.get('j1ed')
        positiondet1 = request.POST.get('positiondet1')
        references = request.POST.get('references')
        user=request.user
        template="resume.html"
        print(11)
        create_resume = createResume(user=user,template=template,name=name,comname1=comname1,comname2=comname2,comname3=comname3, address=address, phone=phone, email=email, aboutyou=aboutyou, careerobj=careerobj, ssc=ssc, hsc=hsc, college=college, degree=degree, cgpa=cgpa, j3sd=j3sd,j3ed=j3ed, positiondet3=positiondet3, j2sd=j2sd, j2ed=j2ed, positiondet2=positiondet2, j1sd=j1sd, j1ed=j1ed, positiondet1=positiondet1, references=references)
        print(12)
        create_resume.save()
        messages.success(request, "Your Info has been saved")
    return render(request, "create-resume.html")

def resume(request):
    try:
        print("hello")
        resume_info = createResume.objects.filter(user = request.user).first()
        print(resume_info.__dict__)
        context = {"resume_info": resume_info}
        return render(request, "resume.html", context)
    except Exception as e:
        print(e)
        print("hello2")
        return render(request, "resume.html")


def resumeindex(request):
    return render(request,"resumeindex.html")