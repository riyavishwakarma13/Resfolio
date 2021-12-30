from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from Portfolio.models import Createportfolio
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from .serializers import templateserializer
from django.contrib.auth.decorators import login_required
from Portfolio.serializers import templateserializer

# Create your views here.

def register(request):
    if request.method == "POST":
        print("Test 11")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        return redirect("/")
    return render(request, "register.html")

def loginuser(request):
    if request.method == "POST":
        print("Test1")
        username = request.POST.get('username')
        password = request.POST.get('password')
        # check if user have entered login credentials
        User = authenticate(username=username, password=password)
        print("Test2")
        print(username,password)
        if User is not None:
            login(request, User)
            # A backend authenticated the credentials
            return redirect("/choose/")
        else:
            # No backend authenticated the credentials
            return redirect("/login/")
    return render(request, "login.html")

def logoutuser(request):
    logout(request)
    print("logged out")
    return redirect("/login/")


def template(request):
    if templateserializer == "Template-1":
        return render(request, "pt-1.html")
    elif templateserializer == "Template-2":
        return render(request, "pt-2.html")
    elif templateserializer == "Template-3":
        return render(request, "pt-3.html")
    else:
        return HttpResponse("No Template Found")

def portfolio_det(request):
    print("test1")
    if request.method == "POST":
        print("test2")
        user=request.user
        template_url=request.POST.get('template_url')
        print(template_url)
        name=request.POST.get('name')
        prof=request.POST.get('prof')
        about_info=request.POST.get('about_info')
        p1_title=request.POST.get('p1_title')
        p1_content=request.POST.get('p1_content')
        p1_url=request.POST.get('p1_url')
        p2_title=request.POST.get('p2_title')
        p2_content=request.POST.get('p2_content')
        p2_url=request.POST.get('p2_url')
        p3_title=request.POST.get('p3_title')
        p3_content=request.POST.get('p3_content')
        p3_url=request.POST.get('p3_url')
        instagram=request.POST.get('instagram')
        github=request.POST.get('github')
        linkedin=request.POST.get('linkedin')
        gmail=request.POST.get('gmail')
        templates=request.POST['templates']
        createp= Createportfolio(user=user,template_url=template_url,templates=templates,name=name,prof=prof,about_info=about_info,p1_title=p1_title,p1_content=p1_content,p1_url=p1_url,p2_title=p2_title,p2_content=p2_content,p2_url=p2_url,p3_title=p3_title,p3_content=p3_content,p3_url=p3_url,instagram=instagram,github=github,linkedin=linkedin,gmail=gmail)
        print("test3")
        createp.save()
        print("test4")
        portfolio_info = templateserializer(createp).data
        context = {"portfolio_info":portfolio_info}
        print(templates)
        info = request.build_absolute_uri(request.get_full_path()).strip(request.get_full_path())+"/portfolio/"+template_url+"/"
        print(info)
        messages.success(request, f"Your Info has been saved.Go to {info} to view the portfolio")
    return render(request, "create-portfolio.html")


@login_required
def portfolio(request, portfolio_url=None):
    try:
        print(portfolio_url)
        if portfolio_url:
            portfolio_info = Createportfolio.objects.filter(template_url = portfolio_url)
        else:
            if not request.user.is_authenticated:
                messages.info(request,"<h1>Enter a valid portfolio url or login to see your own portfolio</h1>")
                return HttpResponseRedirect("/login/")
            portfolio_info = Createportfolio.objects.filter(user= request.user)
            if portfolio_info.exists():
                portfolio_info= templateserializer(portfolio_info[0]).data                
                print(portfolio_info["template_url"])
                print(portfolio_info)
                return HttpResponseRedirect("/portfolio/"+portfolio_info["template_url"])
            else:
                return HttpResponse("<h1>Create a portfolio first</h1>")
        if portfolio_info.exists():  
            portfolio_info= templateserializer(portfolio_info[0]).data
            # print(portfolio_info.__dict__)
            print(portfolio_info)
            context = {"portfolio_info": portfolio_info}
            if portfolio_info["templates"] in ["Template-1",1,"1",'1']:
                print("Still working")
                return render(request, "pt-1.html",context)
            elif portfolio_info["templates"] in ["Template-2",2,"2",'2']:
                return render(request, "pt-2.html",context)
            elif portfolio_info["templates"] in ["Template-3",3,"3",'3']:
                return render(request, "pt-3.html",context)
            else: 
                return HttpResponse("<h1>Template Not Found</h1>")
        else:
            return HttpResponse("<h1>No such portfolio found</h1>")
    except Exception as e:
        print(e)
        print("hello2")
        return render(request, "pt-1.html")

def portfolioindex(request):
    return render(request, "portfolioindex.html")

def core(request):
    return render(request, "core.html")

@login_required
def choose(request):
    return render(request, "choose.html")