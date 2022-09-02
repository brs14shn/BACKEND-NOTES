# PRECLASS SETUP
​
```bash
# CREATING VIRTUAL ENVIRONMENT
# windows
py -m venv env
# windows other option
python -m venv env
# linux / Mac OS
python3 -m venv env
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
python -m django --version
django-admin startproject forms .
```
​
add a gitignore file at same level as env folder
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
go to terminal
​
```bash
py manage.py migrate
py manage.py runserver
```
​
click the link with CTRL key pressed in the terminal and see django rocket.
​
go to terminal, stop project, add app
​
```
py manage.py startapp student
```
​
go to settings.py and add 'student' app to installed apps and add below lines
​
```python
import os
MEDIA_ROOT = os.path.join(BASE_DIR, 'media') or
MEDIA_ROOT = BASE_DIR / 'media/'
MEDIA_URL = '/media/'
```
​
create these folders at project level as /media/
​
go to students/models.py
​
```python
from django.db import models
​
class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    number = models.IntegerField(blank=True, null=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
​
    def __str__(self):
        return f"{self.last_name} {self.first_name}"
​
```
​
go to terminal
​
```bash
pip install pillow
pip freeze > requirements.txt
py manage.py makemigrations
py manage.py migrate
python manage.py createsuperuser
```
​
navigate to admin panel and show that student model does not exist
​
go to student/admin.py
​
```python
from django.contrib import admin
​
from .models import Student
# Register your models here.
admin.site.register(Student)
```
​
to see the picture on browser.
​
go to forms/urls.py
​
```python
from django.conf import settings
from django.conf.urls.static import static
​
urlpatterns = [
    # ... the rest of your URLconf goes here ...
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```
​
create template folder as student/templates/student
​
base.html
​
```html
<!DOCTYPE html>
{% load static %}
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
    <!-- <link rel="stylesheet" href="../static/css/style.css" /> -->
    <link rel="stylesheet" href="{% static 'student/css/style.css' %}" />
  </head>
  <body>
    {% block container %}{% endblock container %}
  </body>
</html>
```
​
index.html
​
```html
{% extends "student/base.html" %} {% block container %}
<h1>Home Page</h1>
​
<h3>Student App</h3>
​
{% endblock container %}
```
​
student.html
​
```html
{% extends "student/base.html" %} {% block container %}
<form action="">
  <label for="">student name</label>
  <input type="text" name="name" />
  <input type="submit" value="OK" />
</form>
{% endblock container %}
```
​
go to student/views.py
​
```python
from django.shortcuts import render
​
def index(request):
    return render(request, 'student/index.html')
​
def student_page(request):
    return render(request,'student/student.html')
​
```
​
go to forms/urls.py
​
```python
from django.contrib import admin
from django.urls import path, include
​
from student.views import index
​
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('student/', include('student.urls')),
]
```
​
go to student/urls.py
​
```python
from django.urls import path
​
from .views import student_page
​
urlpatterns = [
    path('', student_page, name='student'),
]
```
​
run server and explain urls and form.html
​
go to students/forms.py
​
```python
from django import forms
from .models import Student
​
class StudentForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    number = forms.IntegerField(required=False)
    profile_image = forms.ImageField(required=False)
```
​
go to student/views.py and amend student_page
​
```python
from .forms import StudentForm
​
def student_page(request):
    form = StudentForm()
    context = {
        'form': form
    }
    return render(request,'student/student.html', context)
```
​
explain sending form
​
go to student/templates/student/student.html and amend below lines
​
```html
% extends "student/base.html" %} {% block container %}
​
<h2>Student Form</h2>
​
{% comment %}
<form action="">
  <label for="">student name</label>
  <input type="text" />
  <input type="submit" value="OK" />
</form>
{% endcomment %}
​
<form action="" method="post" enctype="multipart/form-data">
  {% csrf_token %} {{ form.as_p }}
  <input type="submit" value="OK" />
</form>
​
{% endblock container %}
```
​
explain get, post, enctype and CSRF
​
go to student/views.py and amend student_page
​
```python
def student_page(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            student_data = {
                "first_name": form.cleaned_data.get('first_name'),
                "last_name": form.cleaned_data.get('last_name'),
                "number": form.cleaned_data.get('number'),
                "profile_pic": form.cleaned_data.get('profile_image'),
            }
            student = Student(**student_data)
            student.save()
            return redirect('student')
​
    context = {
        'form': form
    }
    return render(request, 'student/student.html', context)
```
​
explain POST, and how to save student
​
navigate to admin panel and show student model there and display recorded students
​
go to student/forms.py and amend StudentForm and use forms.ModelForm class
​
```python
from .models import Student
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["first_name", "last_name", "number", "profile_pic"]
        labels = {"first_name": "Name"}
```
​
go to student/views.py and amend student_page
​
```python
def student_page(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('student')
​
    context = {
        'form': form
    }
    return render(request, 'student/student.html', context)
```
​
explain form.save and request FILES
​
## BOOTSTRAP
​
go to student/templates/student/base.html and add bootstrap
​
```html
<!DOCTYPE html>
{% load static %}
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
    <!-- <link rel="stylesheet" href="../static/css/style.css" /> -->
    <link rel="stylesheet" href="{% static 'student/css/style.css' %}" />
    <!-- CSS only -->
    <link
      href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css"
      rel="stylesheet"
      integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3"
      crossorigin="anonymous"
    />
  </head>
​
  <body>
    <div style="margin-top: 100px; margin-bottom: 100px" class="container">
      {% block container %}{% endblock container %}
    </div>
    <!-- JavaScript Bundle with Popper -->
    <script
      src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"
      integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p"
      crossorigin="anonymous"
    ></script>
  </body>
</html>
```
​
## CRISPY FORMS
​
go to terminal
​
```bash
pip install django-crispy-forms
pip freeze > requirements.txt
```
​
go to settings.py
​
```python
INSTALLED_APPS = (
    ...
    'crispy_forms',
)
​
CRISPY_TEMPLATE_PACK = 'bootstrap4'
```
​
go to student/templates/student/student.html and crispy tags
​
```html
{% extends "student/base.html" %} {% block container %}
​
<h2>Student Form</h2>
​
{% comment %}
<form action="">
  <label for="">student name</label>
  <input type="text" />
  <input type="submit" value="OK" />
</form>
{% endcomment %}
<div style="width:300px;">
  {% load crispy_forms_tags %}
  <form action="" method="post" enctype="multipart/form-data">
    {% csrf_token %} {% comment %} {{ form.as_p }} {% endcomment %} {{ form |
    crispy}}
    <input type="submit" value="OK" />
  </form>
</div>
{% endblock container %}
```
## MESSAGES
​
go to student/views.py and import messages end send success message
​
```python
# from django.contrib import messages
def student_form(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Student added successful")
            return redirect('/student/')
    context = {
        'form': form
    }
    return render(request, 'student/student.html', context)
```
​
go to student/templates/student/base.html and add messages codes
​
```html
<!DOCTYPE html>
{% load static %}
<html lang="en">
​
<head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
    <!-- <link rel="stylesheet" href="../static/css/style.css" /> -->
    <link rel="stylesheet" href="{% static 'student/css/style.css' %}" />
    <!-- CSS only -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
</head>
​
<body>
    <div style="margin-top: 10px; margin-bottom: 10px" class="container">
        {% if messages %}
        {% for message in messages %}
        {% if message.tags == "error" %}
        <div class="alert alert-danger">{{ message }}</div>
        {% else %}
        <div class="alert alert-{{ message.tags }}">{{ message }}</div>
        {% endif %}
        {% endfor %}
        {% endif %}
        {% block container %}{% endblock container %}
    </div>
    <!-- JavaScript Bundle with Popper -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"
        integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous">
    </script>
    </script>
    <script src="{% static 'student/js/timeout.js' %}"></script>
</body>
​
</html>
```