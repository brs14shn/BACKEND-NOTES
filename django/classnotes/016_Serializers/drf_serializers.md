## What is API?

An application programming interface is a connection between computers or between computer programs.

It is a type of software interface, offering a service to other pieces of software.

A document or standard that describes how to build such a connection or interface is called an API specification.

API is **the messenger that delivers your request to the provider that you're requesting it from and then delivers the response back to you**.

What is REST API?

An API, or _application programming interface_, is a set of rules that define how applications or devices can connect to and communicate with each other. A REST API is an API that conforms to the design principles of the REST, or _representational state transfer_ architectural style. For this reason, REST APIs are sometimes referred to RESTful APIs*.*

First defined in 2000 by computer scientist Dr. Roy Fielding in his doctoral dissertation, REST provides a relatively high level of flexibility and freedom for developers. This flexibility is just one reason why REST APIs have emerged as a common method for connecting components and applications in a [microservices](https://www.ibm.com/cloud/learn/microservices) architecture.

At the most basic level, an [API](https://www.ibm.com/cloud/learn/api) is a mechanism that enables an application or service to access a resource within another application or service. The application or service doing the accessing is called the client, and the application or service containing the resource is called the server.

Some APIs, such as SOAP or XML-RPC, impose a strict framework on developers. But REST APIs can be developed using virtually any programming language and support a variety of data formats. The only requirement is that they align to the following six REST design principles - also known as architectural constraints:

1. **Uniform interface**. All API requests for the same resource should look the same, no matter where the request comes from. The REST API should ensure that the same piece of data, such as the name or email address of a user, belongs to only one uniform resource identifier (URI). Resources shouldn’t be too large but should contain every piece of information that the client might need.

2. **Client-server decoupling**. In REST API design, client and server applications must be completely independent of each other. The only information the client application should know is the URI of the requested resource; it can't interact with the server application in any other ways. Similarly, a server application shouldn't modify the client application other than passing it to the requested data via HTTP.

3. **Statelessness**. REST APIs are stateless, meaning that each request needs to include all the information necessary for processing it. In other words, REST APIs do not require any server-side sessions. Server applications aren’t allowed to store any data related to a client request.

4. **Cacheability**. When possible, resources should be cacheable on the client or server side. Server responses also need to contain information about whether caching is allowed for the delivered resource. The goal is to improve performance on the client side, while increasing scalability on the server side.

5. **Layered system architecture**. In REST APIs, the calls and responses go through different layers. As a rule of thumb, don’t assume that the client and server applications connect directly to each other. There may be a number of different intermediaries in the communication loop. REST APIs need to be designed so that neither the client nor the server can tell whether it communicates with the end application or an intermediary.

6. **Code on demand (optional)**. REST APIs usually send static resources, but in certain cases, responses can also contain executable code (such as Java applets). In these cases, the code should only run on-demand.

## INCLASS STARTS

```bash
# CREATING VIRTUAL ENVIRONMENT
# windows
py -m venv env
# windows other option
python -m venv env
# linux / Mac OS
vitualenv env

# ACTIVATING ENVIRONMENT
# windows
.\env\Scripts\activate
# linux / Mac OS
source env/bin/activate

# PACKAGE INSTALLATION
# if pip does not work try pip3 in linux/Mac OS
pip install django
# alternatively python -m pip install django
pip install python-decouple
pip freeze > requirements.txt
django-admin --version
django-admin startproject main .
```

## gitignore

add a gitignore file at same level as env folder, and check that it includes .env and /env lines

## Python Decouple

create a new file and name as .env at same level as env folder

copy your SECRET_KEY from settings.py into this .env file. Don't forget to remove quotation marks from SECRET_KEY

```
SECRET_KEY = django-insecure-)=b-%-w+0_^slb(exmy*mfiaj&wz6_fb4m&s=az-zs!#1^ui7j
```

go to settings.py, make amendments below

```python
from decouple import config

SECRET_KEY = config('SECRET_KEY')
```

go to terminal

```bash
py manage.py migrate
py manage.py runserver
```

click the link with CTRL key pressed in the terminal and see django rocket.

## ADDING AN APP

go to terminal

```
py manage.py startapp student_api
```

go to settings.py and add 'student_api' app to installed apps

go to student_api.models.py

```python
from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    number = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.last_name} {self.first_name}"

```

go to student_api.admin.py

```python
from django.contrib import admin
from .models import Student
# Register your models here.

admin.site.register(Student)
```

go to terminal

```bash
pip install djangorestframework
```

go to settings.py and add 'rest_framework' to installed apps

## Serializers

Serializers allow complex data such as querysets and model instances to be converted to native Python datatypes that can then be easily rendered into JSON, XML or other content types. Serializers also provide deserialization, allowing parsed data to be converted back into complex types, after first validating the incoming data.

## Declaring Serializers with serializers.Serializer

create serializers.py under student_api

```python
from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=30)
    last_name = serializers.CharField(max_length=30)
    number = serializers.IntegerField(required=False)
    
    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.number = validated_data.get('number', instance.number)
        instance.save()
        return instance
```

## ModelSerializer

go to serializers.py and make below amendments

```python
from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ["id", "first_name", "last_name", "number"]
        # fields = '__all__'
        # exclude = ['number']
```

go to student_api.views.py

```python
from django.shortcuts import render, HttpResponse, get_object_or_404

from .models import Student

from .serializers import StudentSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


def home(request):
    return HttpResponse('<h1>API Page</h1>')

@api_view(['GET', 'POST'])
def student_api(request):
    if request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "message": f"Student {serializer.validated_data.get('first_name')} saved successfully!"}
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE', 'PATCH'])
def student_api_get_update_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "message": f"Student {student.last_name} updated successfully"
            }
            return Response(data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PATCH':
        serializer = StudentSerializer(student, data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            data = {
                "message": f"Student {student.last_name} updated successfully"
            }
            return Response(data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        student.delete()
        data = {
            "message": f"Student {student.last_name} deleted successfully"
        }
        return Response(data)
```

go to main.urls.py

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('student_api.urls')),
]
```

go to student_api.urls.py

```python
from django.urls import path
from .views import home,student_api, student_api_get_update_delete

urlpatterns = [
    path('', home),
    path('student/', student_api),
    path('student/<int:pk>/', student_api_get_update_delete, name = "detail")
]
```

go to terminal

```bash
py manage.py makemigrations
py manage.py migrate
pip freeze > requirements.txt
py manage.py createsuperuser
py manage.py runserver
```

## Relational fields

go to student_api.models.py and make below amendments

```python
from django.db import models

class Path(models.Model):
    path_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.path_name}"

class Student(models.Model):
    path = models.ForeignKey(Path, related_name='students', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    number = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.last_name} {self.first_name}"
```

go to student_api.serializers.py and make below amendments

```python
from rest_framework import serializers
from .models import Student, Path

class PathSerializer(serializers.ModelSerializer):
    class Meta:
        model = Path
        fields = ["id", "path_name"]

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"
```

**Delete db.sqlite3**<br>
**Delete 0001_initial.py** under student_api/migrations

go to terminal

```bash
py manage.py makemigrations
py manage.py migrate
py manage.py createsuperuser
py manage.py runserver
```


Add path_api view to views.py

```
@api_view(['GET', 'POST'])
def path_api(request):
    # from rest_framework.decorators import api_view
    # from rest_framework.response import Response
    # from rest_framework import status

    if request.method == 'GET':
        paths = Path.objects.all()
        serializer = PathSerializer(paths, many=True, context={'request': request})
        return Response(serializer.data)
    elif request.method == 'POST':
        # from pprint import pprint
        # pprint(request)
        serializer = PathSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "message": f"Path saved successfully!"}
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
```

Don't forget to update urls.py

### StringRelatedField

StringRelatedField may be used to represent the target of the relationship using its **str** method.

go to student_api.serializers.py and make below amendments

```python
from rest_framework import serializers
from .models import Student, Path

class PathSerializer(serializers.ModelSerializer):
    students = serializers.StringRelatedField(many=True)
    class Meta:
        model = Path
        fields = "__all__"

class StudentSerializer(serializers.ModelSerializer):
    path = serializers.StringRelatedField()
    class Meta:
        model = Student
        fields = "__all__"
```



### PrimaryKeyRelatedField

PrimaryKeyRelatedField may be used to represent the target of the relationship using its primary key.

go to student_api.serializers.py and make below amendments

```python
from rest_framework import serializers
from .models import Student, Path

class PathSerializer(serializers.ModelSerializer):
    students = serializers.PrimaryKeyRelatedField(read_only=True, many=True)
    class Meta:
        model = Path
        fields = "__all__"

class StudentSerializer(serializers.ModelSerializer):
    path = serializers.StringRelatedField()
    class Meta:
        model = Student
        fields = "__all__"
```

## BONUS SECTION : WHAT IS CORS?

Cross-Origin Resource Sharing (CORS) is an HTTP-header based mechanism that allows a server to indicate any origins (domain, scheme, or port) other than its own from which a browser should permit loading resources.
For security reasons, browsers restrict cross-origin HTTP requests initiated from scripts.
When a browser load a page, if a script in that page tries to reach another url/origin, browser asks the traget url/origin whether it accepts this request or not.
So, we need to make some amendmetns in our app to talk to a browser and allow them to send requests.

## CORS SETUP IN DJANGO

```bash
pip install django-cors-headers
```

settings.py

```python
ALLOWED_HOSTS = ['*']
INSTALLED_APPS = [
    # ...
    'corsheaders',
]
MIDDLEWARE = [
    # ...
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    # ...
]
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True
CORS_EXPOSE_HEADERS = (
    'Access-Control-Allow-Origin: *',
)
```

## How to Send Request to Our API with AXIOS

index.html

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link
      href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css"
      rel="stylesheet"
      integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC"
      crossorigin="anonymous"
    />
    <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>

    <title>Document</title>
  </head>
  <body>
    <div class="container">
      <div id="message"></div>
      <div id="userinfo"></div>
      <div style="width: 50%">
        <form id="form">
          <div class="mb-3">
            <label for="name" class="form-label">First Name</label>
            <input type="text" class="form-control" name="name" id="name" />
          </div>
          <div class="mb-3">
            <label for="lastname" class="form-label">Last Name</label>
            <input
              type="text"
              class="form-control"
              name="lastname"
              id="lastname"
            />
          </div>
          <div class="mb-3">
            <label for="number" class="form-label">Number</label>
            <input
              type="number"
              class="form-control"
              name="number"
              id="number"
            />
          </div>

          <button type="submit" class="btn btn-primary" id="addBtn">Add</button>
          <button type="button" class="btn btn-primary" id="updateBtn">
            Update
          </button>
          <button type="button" class="btn btn-danger" id="deleteBtn">
            Delete
          </button>
        </form>
      </div>
      <br />
      <br />
      <div id="studentContainer"></div>
      <br />
      <br />
      <div style="width: 50%">
        <form id="registerForm">
          <div class="mb-3">
            <label for="username" class="form-label">Username</label>
            <input
              type="text"
              class="form-control"
              name="username"
              id="username"
            />
          </div>
          <div class="mb-3">
            <label for="password" class="form-label">Password</label>
            <input
              type="password"
              class="form-control"
              name="password"
              id="password"
            />
          </div>
          <button type="submit" class="btn btn-primary" id="loginBtn">
            Login
          </button>
          <button type="button" class="btn btn-primary" id="registerBtn">
            Register
          </button>
        </form>
      </div>
    </div>

    <script
      src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js"
      integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM"
      crossorigin="anonymous"
    ></script>
    <script src="app.js"></script>
  </body>
</html>
```

app.js

```js
let studentsData;
let id;
let pos;
const baseUrl = 'http://127.0.0.1:8000/';
const accountUrl = baseUrl + 'account/';
const studentUrl = baseUrl + 'api/student/';

// const authentication = 'Basic YmFycnk6MQ==';
// let authentication = 'Token c355264a0f91eafebf9f41d02362b7dd2e43466d';
let authentication;

const displayStudents = async () => {
  try {
    const response = await axios({
      method: 'get',
      url: studentUrl,
      // xsrfHeaderName: 'X-CSRFToken',
      // xsrfCookieName: 'XSRF-TOKEN',
      // withCredentials: true,
      headers: { Authorization: authentication },
    });

    console.log(response.status);
    console.log(response);

    studentsData = response.data;

    studentContainer = document.querySelector('#studentContainer');
    html = `<table id="table" style="width:50%" class="table table-success table-striped">
      <thead>
        <tr>
          <th scope="col">#</th>
          <th scope="col">Firstname</th>
          <th scope="col">Lastname</th>
          <th scope="col">Number</th>  
          <th scope="col">Update</th> 
        </tr>
      </thead>
      <tbody>
      `;

    response.data.forEach((element) => {
      html += `      
        <tr>
          <th scope="row">${element.id}</th>
          <td>${element.first_name}</td>
          <td>${element.last_name}</td>
          <td>${element.number}</td>
          <td><input type="radio" name="radioGroup"></td>
        </tr>`;
    });

    html += ' </tbody></table>';
    studentContainer.innerHTML = html;

    const table = document.getElementById('table');
    table.addEventListener('click', (event) => {
      if (event.target.type === 'radio') {
        id = event.target.parentNode.parentNode.childNodes[1].textContent;

        for (let i = 0; i < studentsData.length; i++)
          if (studentsData[i].id == id) {
            pos = i;
            break;
          }
        document.getElementById('name').value = studentsData[pos].first_name;
        document.getElementById('lastname').value = studentsData[pos].last_name;
        document.getElementById('number').value = studentsData[pos].number;
      }
    });
  } catch (err) {
    console.log(err.message);
  }
};

const resetForm = function () {
  document.getElementById('name').value = '';
  document.getElementById('lastname').value = '';
  document.getElementById('number').value = '';
};

const displayMessages = function (message, type) {
  const messageElement = document.querySelector('#message');
  let msg = message;
  if (type === 'danger') {
    const errors = Object.entries(message).reduce(
      (acc, element) => acc + element[0] + ' ' + element[1][0] + ' <br />',
      ''
    );
    msg = errors;
  }
  messageElement.innerHTML = `<div class="alert alert-${type}">${msg}</div>`;
  setTimeout(function () {
    messageElement.style.display = 'none';
  }, 5000);
};

document.getElementById('form').addEventListener('submit', function (event) {
  event.preventDefault();
});

const addUpdateDelete = async function (event) {
  let method;
  let data = {};
  let url = studentUrl;
  switch (event.target.outerText) {
    case 'Add':
      method = 'post';
      break;
    case 'Update':
      method = 'put';
      url += id + '/';
      break;
    case 'Delete':
      method = 'delete';
      url += id + '/';
      break;
  }

  if (['Update', 'Add'].includes(event.target.outerText)) {
    data = new FormData();

    data.append('first_name', document.getElementById('name').value);
    data.append('last_name', document.getElementById('lastname').value);
    data.append('number', document.getElementById('number').value);
  }

  console.log(method, id, url);
  try {
    const response = await axios({
      method: method,
      url: url,
      headers: { Authorization: authentication },
      data: data,
    });
    console.log(response.status);
    displayMessages(response.data.message, 'success');
    displayStudents();
  } catch (err) {
    console.log(err.message);
    displayMessages(err.response.data.message, 'danger');
  }
};

document.getElementById('updateBtn').addEventListener('click', addUpdateDelete);
document.getElementById('deleteBtn').addEventListener('click', addUpdateDelete);
document.getElementById('addBtn').addEventListener('click', addUpdateDelete);

const displayUser = function (user) {
  document.getElementById('userinfo').innerHTML = `
  <div class="card text-white bg-primary mb-3" style="max-width: 18rem;">
  <div class="card-header">Current User</div>
  <div class="card-body">
    <h5 class="card-title">${user}</h5>
    
  </div>
</div>`;
};

document
  .getElementById('registerForm')
  .addEventListener('submit', async function (event) {
    event.preventDefault();
  });

const loginRergister = async function (url) {
  let data = new FormData();

  data.append('username', document.getElementById('username').value);
  data.append('password', document.getElementById('password').value);

  try {
    const response = await axios({
      method: 'post',
      url: url,
      data: data,
    });
    console.log(response.status);
    console.log(response.data.token);
    authentication = 'Token ' + response.data.token;
    displayStudents();
    displayUser(data.get('username'));
    document.getElementById('username').value = '';
    document.getElementById('password').value = '';
  } catch (err) {
    console.log(err.message);
    displayMessages(err.response.data.message, 'danger');
  }
};

const loginRegisterClick = function (event) {
  let url = accountUrl;

  switch (event.target.outerText) {
    case 'Login':
      url += 'login/';
      break;
    case 'Register':
      url += 'register/';
      break;
  }
  loginRergister(url);
};

document
  .getElementById('loginBtn')
  .addEventListener('click', loginRegisterClick);
document
  .getElementById('registerBtn')
  .addEventListener('click', loginRegisterClick);

displayStudents();
```
