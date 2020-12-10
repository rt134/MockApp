"""modProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from app.views import dashboard_view, car_view, mechanic_view, home_view, contact_view
from app.views import car_form_view, mech_form_view,car_payment_view, mech_payment_view
from accounts.views import signup_view,login_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/',dashboard_view, name="dashboard"),
    path('',signup_view, name="signup"),
    path('login/',login_view, name="login"),
    path('home/',home_view, name="home"),
    path('car/',car_view, name="car"),
    path('car/cbooking/',car_form_view, name="carform"),
    path('mechanic/mbooking/',mech_form_view, name="mechform"),
    path('car/cbooking/payment',car_payment_view, name="carpayment"),
    path('mechanic/mbooking/payment',mech_payment_view, name="mechpayment"),
    path('mechanic/',mechanic_view, name="mechanic"),
    path('contact/',contact_view, name="contact"),
]