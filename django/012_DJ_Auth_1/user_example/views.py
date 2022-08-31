from django.shortcuts import render


def home(request):
    return render(request, 'user_example/index.html')

def special(request):
    return render(request, "user_example/special.html")
