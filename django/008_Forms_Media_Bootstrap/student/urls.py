from django.urls import path

from .views import student_page

urlpatterns = [
    path('', student_page, name='student'),
]
