from django.contrib import admin
from django.urls import path
from Portfolio import views

urlpatterns = [
    path("", views.loginuser, name="login"),
    path("login/",views.loginuser, name="login"),
    path("register/", views.register, name="register"),
    path("portfolioindex/", views.portfolioindex, name="index"),
    path("pt-1/",views.template, name="Template-1"),
    path("pt-2/",views.template, name="Template-2"),
    path("pt-3/",views.template, name="Template-3"),
    path("create-portfolio/", views.portfolio_det, name="create-portfolio"),
    path("portfolio/<slug:portfolio_url>/", views.portfolio, name="portfolio"),
    path("portfolio/", views.portfolio, name="userportfolio"),
    path("logout/",views.logoutuser, name="logout"),
    path("core/", views.core, name="core"),
    path("choose/",views.choose, name="choose"),
]
