from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(requset):
    return HttpResponse("<h2 style='text-align:center'>Welcome Home</h2>")

def fscohort(requset):
     return HttpResponse("<h2 style='text-align:center'>Welcome FS11</h2>")

def subfolder(requset):
     return HttpResponse("<h2 style='text-align:center'>Welcome subfolder page</h2>")