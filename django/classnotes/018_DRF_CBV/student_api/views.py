from email.policy import HTTP
from urllib import response
from django.shortcuts import render
# Create your views here.
from .models import Student, Path
from .serializers import StudentSerializer, PathSerializer
from rest_framework.decorators import api_view

from django.shortcuts import render, HttpResponse, get_object_or_404
from rest_framework.response import Response
from rest_framework import status

from rest_framework.views import APIView
from student_api.models import Student
from student_api.serializers import StudentSerializer
from rest_framework import mixins
from rest_framework.generics import GenericAPIView,mixins
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
# Create your views here.
#! CBV VIEWS 👇
def home(request):
    return HttpResponse('<h1>API Page</h1>')

class StudentList(APIView):
    #! request.method == get 👇
    def get(self, request):
        students = Student.objects.all()
        #! We use "many=True" because there is more than one data 👇
        serializer = StudentSerializer(students, many = True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StudentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StudentDetail(APIView):
    def get_obj(self, pk):
        return get_object_or_404(Student, pk=pk)

    def get(self, request, pk):
        student = self.get_obj(pk)
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    def put(self, request, pk):
        student = self.get_obj(pk)
        serializer = StudentSerializer(student, data = request.data)
        if serializer.is_valid():
            serializer.save()
            new_data = serializer.data
            new_data['success'] = f"student {student.last_name} updated successfuly"
            return Response(new_data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        student = self.get_obj(pk)
        student.delete()
        data = {
            "message" : f"student {student.last_name} deleted successfuly"
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)



#! CBV ## GENERİC APIVİEW 👇

class StudentListCreate(mixins.ListModelMixin,mixins.CreateModelMixin,GenericAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
       return self.create(request, *args, **kwargs)



class StudentURD(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    #lookup_field = "pk"
    


#! CBV ##CONCRATE APIVİEW 👇

class StudentConcrateListCreate(ListCreateAPIView):
     queryset = Student.objects.all()
     serializer_class=StudentSerializer


class StudentConcrateURD(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class=StudentSerializer

#! CBV ##VİEWSET 👇
class StudentMVS(ModelViewSet):
     queryset = Student.objects.all()
     for  i in queryset:
        print(i.first_name)
    
     serializer_class=StudentSerializer
     @action(methods=["GET"], detail=False)
     def student_count(self, request):
        count = {
            
                'student-count': self.queryset.count

            #json icinde kac tane eleman oldugunu mu ögrendik 
        }
        return Response(count)



###* FB VİEWS



# @api_view(['GET', 'POST'])
# def student_api(request):
#     if request.method == 'GET':
#         students = Student.objects.all()
#         serializer = StudentSerializer(students, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             data = {
#                 "message": f"Student {serializer.validated_data.get('first_name')} saved successfully!"}
#             return Response(data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET'])
# def student_list(request):
#     students = Student.objects.all()
#     serializer = StudentSerializer(students, many=True)
#     # print(serializer.data)
#     return Response(serializer.data)


# @api_view(['POST'])
# def student_create(request):
#     print(request.data)
#     serializer = StudentSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         data = {
#             "message": f"Student {serializer.validated_data.get('first_name')} saved successfully!"
#         }
#         return Response(data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors)


# @api_view(['GET', 'PUT', 'DELETE', 'PATCH'])
# def student_api_get_update_delete(request, pk):
#     student = get_object_or_404(Student, pk=pk)
#     if request.method == 'GET':
#         serializer = StudentSerializer(student)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'PUT':
#         serializer = StudentSerializer(student, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             data = {
#                 "message": f"Student {student.last_name} updated successfully"
#             }
#             return Response(data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'PATCH':
#         serializer = StudentSerializer(
#             student, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             data = {
#                 "message": f"Student {student.last_name} updated successfully"
#             }
#             return Response(data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE':
#         student.delete()
#         data = {
#             "message": f"Student {student.last_name} deleted successfully"
#         }
#         return Response(data)


# @api_view(['GET'])
# def student_detail(request, pk):
#     # try:
#     #     student = Student.objects.get(pk=pk)
#     # except Objdkdlşdş:
#     #     raise HTTP404
#     student = get_object_or_404(Student, pk=pk)
#     serializer = StudentSerializer(student)
#     return Response(serializer.data, status=status.HTTP_200_OK)


# @api_view(['PUT'])
# def student_update(request, pk):
#     student = get_object_or_404(Student, pk=pk)
#     serializer = StudentSerializer(student, data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         data = {
#             "message": f"Student {student.last_name} updated successfully"
#         }
#         return Response(data, status=status.HTTP_200_OK)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['PATCH'])
# def student_update_partial(request, pk):
#     student = get_object_or_404(Student, pk=pk)
#     serializer = StudentSerializer(student, data=request.data, partial=True)
#     if serializer.is_valid():
#         serializer.save()
#         data = {
#             "message": f"Student {student.last_name} updated successfully"
#         }
#         return Response(data, status=status.HTTP_200_OK)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['DELETE'])
# def student_delete(request, pk):
#     student = get_object_or_404(Student, pk=pk)
#     student.delete()
#     data = {
#         "message": f"Student {student.last_name} deleted successfully..."
#     }
#     return Response(data, status=status.HTTP_200_OK)


# @api_view(['GET', 'POST'])
# def path_api(request):
    # from rest_framework.decorators import api_view
    # from rest_framework.response import Response
    # from rest_framework import status

    # if request.method == 'GET':
    #     paths = Path.objects.all()
    #     serializer = PathSerializer(
    #         paths, many=True, context={'request': request})
    #     return Response(serializer.data)
    # elif request.method == 'POST':
    #     # from pprint import pprint
    #     # pprint(request)
    #     serializer = PathSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         data = {
    #             "message": f"Path saved successfully!"}
    #         return Response(data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

