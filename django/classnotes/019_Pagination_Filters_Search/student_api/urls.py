from django.urls import path,include

from .views import (
    home,
    StudentList,
    StudentDetail,
    StudentListCreate,
    StudentURD,
    StudentLC,
    StudentRUD,
    StudentGRUD,

    # student_api,
    # student_api_get_update_delete, path_api,
    # student_list,
    # student_create,
    # student_detail,
    # student_update,
    # student_update_partial,
    # student_delete,
   

)
from rest_framework import routers
router=routers.DefaultRouter()
router.register('student',StudentGRUD)
urlpatterns = [
    path('', home),

#### CBV URLS ####
    # path('student/',StudentList.as_view()), #APIView
    # path('student/<int:pk>/',StudentDetail.as_view()), #APIView
    # path('student/',StudentListCreate.as_view()), #Generic APIVie
    # path('student/<int:pk>/',StudentURD.as_view()), #Generic APIVie
    # path('student/',StudentLC.as_view()), #Concrate APIVie
    # path('student/<int:pk>/',StudentRUD.as_view()), #Concrate APIVie
    # path('student/', StudentGRUD.as_view({'get': "list"})), #ViewSet
    # path('student/', StudentGRUD.as_view()), #ViewSet
    path('',include(router.urls))

 

#### FBV URLS ####

    # path('student/', student_api),
    # path('student/<int:pk>/', student_api_get_update_delete, name="detail"),
    # path('path/', path_api),
    # path('student_list/', student_list, name='student_list'),
    # path('student_create/', student_create, name='student_create'),
    # path('student_detail/<int:pk>/', student_detail, name='student_detail'),
    # path('student_update/<int:pk>/', student_update, name='student_update'),
    # path('student_update_partial/<int:pk>/',
    #      student_update_partial, name='student_update_partial'),
    # path('student_delete/<int:pk>/', student_delete, name='student_delete'),
 

]
