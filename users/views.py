import logging
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import check_password
from company.models import Company
from .forms import RegisterUserForm
from .models import User
from resume.models import Resume
# Create your views here.


logger = logging.getLogger(__name__)

# Applicants Only Registration


def register_applicants(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            seeker = form.save(commit=False)
            seeker.is_applicant = True
            seeker.username = seeker.email
            seeker.save()
            Resume.objects.create(user=seeker)
            messages.info(request, 'Your Account has been created.')
            return redirect('login')
        else:
            messages.warning(request, 'Something went wrong')
            return redirect('register-applicants')
    else:
        form = RegisterUserForm()
        context = {'form': form}
        return render(request, 'users/register-applicants.html', context)


# Recruiter Registration Only
def recruiter_register(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            hire = form.save(commit=False)
            hire.is_recruiter = True
            hire.username = hire.email
            hire.save()
            Company.objects.create(user=hire)
            messages.info(request, 'Your Account has been created.')
            return redirect('login')
        else:
            messages.warning(request, 'Something went wrong')
            return redirect('register-recruiter')
    else:
        form = RegisterUserForm()
        context = {'form': form}
        return render(request, 'users/register-recruiter.html', context)


# login a user
def login_user(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(request, username=email, password=password)
        if user is not None and user.is_active:
            login(request, user)
            logger.info(f"User {user.email} logged in successfully.")
            return redirect('dashboard')
        else:
            messages.warning(
                request, 'Invalid email or password. Please try again.')
            logger.warning(f"Failed login attempt for email: {email}")
            return redirect('login')
    else:
        return render(request, 'users/login.html')


# logout
def logout_user(request):
    logout(request)
    messages.info(request, 'Thanks for your time')
    return redirect('login')
