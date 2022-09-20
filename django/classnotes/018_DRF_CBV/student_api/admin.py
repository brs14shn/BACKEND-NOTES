from django.contrib import admin

# Register your models here.
from .models import Student,Path
admin.site.register(Student)
admin.site.register(Path)