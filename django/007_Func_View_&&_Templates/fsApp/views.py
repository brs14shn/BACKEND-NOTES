from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


# def home(request):
#     print(request.user)
#     {{request.user}}
#     html = "<h1 style='text-align:center'><body>Hello World!</body></h1>"
#     return HttpResponse(html)

def home(request):
    return render(request, 'fsApp/index.html')
