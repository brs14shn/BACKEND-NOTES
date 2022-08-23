from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def fshome(request):
    return HttpResponse('<p>Hello World</p>')
