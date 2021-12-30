from os import name
from django.contrib import admin
from django.urls import path
from Resume import views

urlpatterns = [
    path("choose/",views.choose, name="choose"),
    path("resumeindex/",views.resumeindex, name="index"),
    path("core/", views.core, name="core"),
    path("contact/", views.contact, name="contact"),
    path("create-resume/",views.resume_det,name="create-resume"),
    path("resume/",views.resume,name="resume"),
]