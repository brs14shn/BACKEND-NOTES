# BASE USER PRECLASS SETUP
​
```bash
# CREATING VIRTUAL ENVIRONMENT
# windows
py -m venv env
# windows other option
python -m venv env
# linux / Mac OS
vitualenv env
​
# ACTIVATING ENVIRONMENT
# windows
.\env\Scripts\activate
# linux / Mac OS
source env/bin/activate
​
# PACKAGE INSTALLATION
# if pip does not work try pip3 in linux/Mac OS
pip install django
# alternatively python -m pip install django
pip install python-decouple
pip install pillow
pip install django-crispy-forms
pip freeze > requirements.txt
django-admin --version
django-admin startproject main .
```
​
go to terminal
​
```bash
py manage.py runserver
```
​
click the link with CTRL key pressed in the terminal and see django rocket.
​
go to terminal, stop project, add app
​
```
py manage.py startapp users
```
​
go to settings.py and add 'users' app and 'crispy_forms' to installed apps and add below lines
​
```python
import os
​
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 3rd party apps,
    'crispy_forms',
    # my apps
    'users',
]
​
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
​
CRISPY_TEMPLATE_PACK = 'bootstrap4'
```
​
create these folders at project level as /media/profile_pics
​
create template folder as users/templates/users
​
base.html
​
```html
<!DOCTYPE html>
{% load static %}
​
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
​
    <link
      rel="stylesheet"
      href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-alpha.6/css/bootstrap.min.css"
      integrity="sha384-rwoIResjU2yc3z8GV/NPeZWAv56rSmLldC3R/AZzGRnGxQQKnKkoFVhFQhNUwEyJ"
      crossorigin="anonymous"
    />
​
    {% comment %}
    <link rel="stylesheet" href=" {% static 'users/css/bootstrap.min.css' %}" />
    {% endcomment %}
​
    <link rel="stylesheet" href=" {% static 'users/css/style.css' %}  " />
​
    <title>Document</title>
  </head>
​
  <body>
    {% include "users/navbar.html" %}
    <div style="margin-top: 100px; margin-bottom: 100px" class="container">
      {% if messages %} {% for message in messages %} {% if message.tags ==
      "error" %}
      <div class="alert alert-danger">{{ message }}</div>
      {% else %}
      <div class="alert alert-{{ message.tags }}">{{ message }}</div>
      {% endif %} {% endfor %} {% endif %} {% block content %} {% endblock
      content %}
    </div>
    <script
      src="https://code.jquery.com/jquery-3.2.1.slim.min.js"
      integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN"
      crossorigin="anonymous"
    ></script>
    <script
      src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js"
      integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q"
      crossorigin="anonymous"
    ></script>
    <script
      src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"
      integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl"
      crossorigin="anonymous"
    ></script>
    <script src="{% static 'users/js/timeout.js' %}"></script>
  </body>
</html>
```
​
home.html
​
```html
{% extends 'users/base.html' %} {% block content %}
<h1>Home Page</h1>
{% if request.user.is_authenticated %}
<h2>Wellcome {{request.user}}!</h2>
{% else %}
<h2>Wellcome Guest!</h2>
{% endif %} {% endblock content %}
```
​
register.html
​
```html
{% extends 'users/base.html' %} {% block content %} {% load crispy_forms_tags %}
​
<h2>Registration Form</h2>
​
{% if request.user.is_authenticated %}
​
<h3>Thanks for registering</h3>
​
{% else %}
​
<h3>Fill out the form please!</h3>
<form action="" method="post" enctype="multipart/form-data">
  {% csrf_token %} {{ form_user | crispy }} {{ form_profile | crispy }}
  <button type="submit" class="btn btn-danger">Register</button>
</form>
{% endif %} {% endblock content %}
```
​
user_login.html
​
```html
{% extends 'users/base.html' %} {% block content %} {% load crispy_forms_tags %}
​
<div class="row">
  <div class="col-md-6 offset-md-3">
    <h3>Please Login</h3>
​
    <form action="{% url 'user_login' %}" method="post">
      {% csrf_token %} {{form|crispy}}
      <button type="submit" class="btn btn-danger">Login</button>
    </form>
  </div>
</div>
{% endblock content %}
```
​
navbar.html
​
```html
{% load static %} {% load static %}
​
<nav class="navbar navbar-toggleable-md navbar-inverse fixed-top bg-inverse">
  <button
    class="navbar-toggler navbar-toggler-right"
    type="button"
    data-toggle="collapse"
    data-target="#navbarCollapse"
    aria-controls="navbarCollapse"
    aria-expanded="false"
    aria-label="Toggle navigation"
  >
    <span class="navbar-toggler-icon"></span>
  </button>
  <a class="navbar-brand" href="{% url 'home'  %}"
    ><img src="{% static 'users/images/cw_logo.jpg' %}" alt="CLARUSWAY_LOGO" />
​
    Clarusway FS</a
  >
​
  <div class="collapse navbar-collapse" id="navbarCollapse">
    <ul class="navbar-nav mr-auto">
      <li class="nav-item active">
        {% comment %} {% url 'students' %} {% endcomment %}
        <a class="nav-link" href="">Students</a>
      </li>
      <li class="nav-item active">
        <a class="nav-link" href="">Contact</a>
      </li>
    </ul>
​
    <ul class="navbar-nav ml-auto">
      {% if request.user.is_authenticated %} {% if request.user.is_superuser %}
​
      <li class="nav-item active">
        <a class="nav-link" href="/admin">Admin</a>
      </li>
      {% endif %}
​
      <li class="nav-item active">
        {% comment %} {% url 'logout' %} {% endcomment %}
        <a class="nav-link" href="">Log Out</a>
      </li>
      {% else %}
​
      <li class="nav-item active">
        {% comment %} {% url 'user_login' %} {% endcomment %}
        <a class="nav-link" href="">Log In</a>
      </li>
      {% endif %}
      <li class="nav-item active">
        {% comment %} {% url 'register' %} {% endcomment %}
        <a class="nav-link" href="">Register</a>
      </li>
    </ul>
  </div>
</nav>
```
​
create folder under users/static/users/images
​
copy cw_logo to this folder
​
go to users.views.py
​
```python
from django.shortcuts import render, redirect, HttpResponse
​
from django.contrib import messages
​
# Create your views here.
​
def home(request):
    return render(request, 'users/home.html')
```
​
go to main/urls.py
​
```python
from django.contrib import admin
from django.urls import path, include
from users.views import home
from django.conf.urls.static import static
from django.conf import settings
​
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('users/', include('users.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```
​
go to users.urls.py
​
```python
from django.urls import path
​
urlpatterns = [
]
```
​
go to terminal and run server
​
```bash
py manage.py runserver
```
​
## gitignore
​
add a gitignore file at same level as env folder, and check that it includes .env and /env lines
​
## Python Decouple
​
create a new file and name as .env at same level as env folder
​
copy your SECRET_KEY from settings.py into this .env file. Don't forget to remove quotation marks from SECRET_KEY
​
```
SECRET_KEY = django-insecure-)=b-%-w+0_^slb(exmy*mfiaj&wz6_fb4m&s=az-zs!#1^ui7j
```
​
go to settings.py, make amendments below
​
```python
from decouple import config
​
SECRET_KEY = config('SECRET_KEY')
```
​
# INCLASS STARTS
​
## Extending the Default User Model
​
1. Using a Proxy Model
2. Creating a New Table and Using OneToOneField with User Model
3. Adding New Fields to Default User by Using AbstractUser
4. Redefining Default User from Scratch by Using AbstractBaseUser
​
## Creating a New Table and Using OneToOneField with User Model
​
go to users.models.py
​
```python
from django.db import models
from django.contrib.auth.models import User
​
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    portfolio = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
    def __str__(self):
        return self.user.username
```
​
go to users/admin.py
​
```python
from django.contrib import admin
from .models import UserProfile
# Register your models here.
admin.site.register(UserProfile)
```
​
go to users.forms.py
​
~~~python
from django import forms
from .models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
​
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
​
class UserForm(UserCreationForm):
    class Meta():
        model = User
        fields = ('username', 'email') 
​
class UserProfileForm(forms.ModelForm):
    class Meta():
        model = UserProfile
        # fields = '__all__'
        exclude = ('user',)
~~~
​
go to users.views.py
​
```python
from django.shortcuts import render, redirect, HttpResponse
​
from .forms import UserProfileForm, UserForm, LoginForm
from django.contrib.auth.models import User
​
# login imports
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
​
from django.contrib import messages
​
# Create your views here.
def home(request):
    return render(request, 'users/home.html')
​
def register(request):
​
    form_user = UserForm(request.POST or None)
    form_profile = UserProfileForm(request.POST or None)
    if form_user.is_valid() and form_profile.is_valid():
​
        user = form_user.save()
​
        profile = form_profile.save(commit=False)
        profile.user = user
​
        if 'profile_pic' in request.FILES:
            profile.profile_pic = request.FILES['profile_pic']
​
        profile.save()
        messages.success(request, "Register successful")
        return redirect('home')
​
    context = {
        'form_profile': form_profile,
        'form_user': form_user
    }
​
    return render(request, 'users/register.html', context)
​
​
def user_login(request):
​
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
​
        user = authenticate(username=username, password=password)
​
        if user:
            messages.success(request, "Login successful")
            login(request, user)
            return redirect('home')
​
            # if user.is_active:
            #     messa...