from django.shortcuts import HttpResponse
from .models import Student
from .serializers import StudentSerializer
from rest_framework import generics

from rest_framework.permissions import (
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly
    )

from .permissions import IsAdminorReadOnly,IsAddedByUserOrReadOnly



# Create your views here.
def home(request):
    return HttpResponse('<h1>API Page</h1>')

class StudentList(generics.ListCreateAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()

    #! Custom Permissons
    
    #permission_classes = [IsAdminorReadOnly]
    
    
    
    permission_classes = [IsAuthenticated]
    
    # login olmadan istek döndürülmez

    # permission_classes = [IsAdminUser]
    # Login olmak yeterli değil admin olmak zorunda 

    #permission_classes = [IsAuthenticatedOrReadOnly]
    # Login olmadığında sadece get isteği yapar
     
     #! Login olmuş kullanıcıyı ekliyorum.
    def perform_create(self,serializer):
        serializer.save(user=self.request.user)


       

class StudentOperations(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
    permission_classes = [IsAddedByUserOrReadOnly]
