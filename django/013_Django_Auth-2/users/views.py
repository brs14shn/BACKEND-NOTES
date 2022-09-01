from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
# Create your views here.
from django.contrib import messages

def home(request):
    return render(request, 'users/home.html')

def user_logout(request):
    messages.success(request, 'You logged out!')
    logout(request)
    return redirect("home")