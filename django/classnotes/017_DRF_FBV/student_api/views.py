from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponse, get_object_or_404

from .models import Student,Path

from .serializers import StudentSerializer,PathSerializer
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




@api_view(['GET'])
def student_list(request):
   #students=Student.objects.filter(path=1)  # FullStack öğrenciler
   students=Student.objects.all() #tüm öğrenciler
   serializer=StudentSerializer(students,many=True) # birden fazla data olduğunu belirttik.
   return Response(serializer.data)
   print(serializer.data)

@api_view(['POST'])
def student_create(request):
    print(request.data)
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        data = {
            "message": 'Student create succesfully.....'
        }
        return Response(data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors)

@api_view(['GET'])
def student_detail(request, pk):
    # try:
    #     student = Student.objects.get(pk=pk)
    # except Objdkdlşdş:
    #     raise HTTP404
    student = get_object_or_404(Student, pk=pk)
     #!get_object_or_404() işlevi, ilk öğe olarak bir
    #!Django modeli ve model yöneticisinin get() değişkeni alır. Nesne yoksa Http404'ü #yükseltir.
    serializer = StudentSerializer(student)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['PUT'])
def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    serializer = StudentSerializer(instance=student,data=request.data)
    if serializer.is_valid():
        serializer.save()
        data = {
                "message": f"Student {serializer.validated_data.get('first_name')} saved successfully!"}
        return Response(data, status=status.HTTP_201_CREATED)
    # valid değilse
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    student.delete()
    data = {
        "message": f"Student {student.last_name} deleted successfully..."
    }
    return Response(data, status=status.HTTP_200_OK) 



