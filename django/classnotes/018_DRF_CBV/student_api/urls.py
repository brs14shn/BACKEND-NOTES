from django.urls import path,include
from rest_framework import routers
from .views import (
    home,
    StudentList,
    StudentDetail,

    StudentListCreate,
    StudentURD,


    StudentConcrateListCreate,
    StudentConcrateURD,


    StudentMVS





    ##* FBV
    # student_api,
    # student_api_get_update_delete, path_api,
    # student_list,
    # student_create,
    # student_detail,
    # student_update,
    # student_update_partial,
    # student_delete
)

router = routers.DefaultRouter()
router.register('student', StudentMVS )

urlpatterns = [
    path('', home),
    ###* FB URLS
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

    ###* CB URLS API VİEW
    #path("student/",StudentList.as_view()),
    # path('detail/<int:pk>/', StudentDetail.as_view()),

    ###* CB URLS GENERİC APIVİEW
    # path("list/",StudentListCreate.as_view()),
    # path("urd/<int:pk>",StudentURD.as_view()),


    #! CBV ##CONCRATE APIVİEW 👇
    # path("list/",StudentConcrateListCreate.as_view()),
    # path("urd/<int:pk>",StudentConcrateURD.as_view()),


    #! CBV ##VİEWSET
    # path("student/",StudentMVS.as_view({
    # 'get': 'list',
    # 'put': 'update',
    # 'patch': 'partial_update',
    # 'delete': 'destroy'
    # }))
   # kısa yolu
   path("",include(router.urls))




]
