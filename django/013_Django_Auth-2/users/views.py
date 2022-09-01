from django.shortcuts import render

# Create your views here.
from django.contrib import messages

def home(request):
    return render(request, 'users/home.html')