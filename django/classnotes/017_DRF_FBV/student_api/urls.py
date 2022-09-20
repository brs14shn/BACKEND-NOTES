from django.urls import path
from .views import (
    home,
    student_api,
    student_api_get_update_delete,
    path_api,


    student_list,
    student_create,
    student_detail,
    student_update,
    student_delete
     
     )

urlpatterns = [
    path('', home),
    path('student/', student_api),
    path('student/<int:pk>/', student_api_get_update_delete, name = "detail"),
    path('path/', path_api),
    path("student_list/",student_list,name="student_list"),
    path("student_create/",student_create,name="student_create"),
    path("student_detail/<int:pk>/",student_detail,name="student_detail"),
    path("student_update/<int:pk>/",student_update,name="student_update"),
    path("student_delete/<int:pk>/",student_delete,name="student_delete"),

]