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
python manage.py migrate
python manage.py runserver
```
​
click the link with CTRL key pressed in the terminal and see django rocket.
​
go to terminal, stop project, add app
​
```
python manage.py startapp student
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
```
# IMAGE FİELD
  1- İnstall python -m pip install Pillow 
  2- main >> settings.py >> MEDİA_URL="upload_to verilen ismi ekle"
  3- main >>urls.py file içerisine 👇
  # View Static/Media Files:
    from django.conf import settings
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) komut eklenir.
```