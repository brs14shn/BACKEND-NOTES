from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


def home(request):
    return render(request, 'user_example/index.html')

def special(request):
    return render(request, "user_example/special.html")

def register(request):
    form=UserCreationForm()
    context={
        "form":form
    }

    return render(request,"registration/register.html",context)
