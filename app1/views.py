from django.shortcuts import render

# Create your views here.
# user_auth/views.py

from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import SignupForm, LoginForm
from .models import User

def HomePage(request):
    return render(request,'home.html')

def doctorsignup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            messages.success(request, 'Account created successfully. Please login.')
            return redirect('login')
    else:
        form = SignupForm()

    return render(request, 'signupdoctor.html', {'form': form})

def patientsignup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            messages.success(request, 'Account created successfully. Please login.')
            return redirect('login')
    else:
        form = SignupForm()

    return render(request, 'signuppatient.html', {'form': form})

def LoginPage(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = User.objects.filter(username=username, password=password).first()

            if user:
                # Redirect to user's dashboard based on user type
                return redirect(f'{user.user_type}_dashboard', user_id=user.id)
            else:
                messages.error(request, 'Invalid login credentials')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})

def patientlogin(request):
    return render(request, 'patient.html')

def doctorlogin(request):
    return render(request, 'doctor.html')
