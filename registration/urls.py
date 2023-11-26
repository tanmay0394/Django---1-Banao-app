"""
URL configuration for registration project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from app1 import views
from doctorsignup.views import signaction
from doctorlogin.views import loginaction
from patientsignup.views import signaction
from patientlogin.views import loginaction


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.HomePage,name = 'homepage'),
    path('login/',views.LoginPage,name = 'login'),
    path('patientlogin/',views.patientlogin,name = 'patientdashboard'),
    path('doctorlogin/',views.doctorlogin,name = 'doctordashboard'),
    path('patientsignup/',views.patientsignup,name = 'patientdashboard'),
    path('doctorsignup/',views.doctorsignup,name = 'doctorsignup')
]