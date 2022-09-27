from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import RegistrationSerializer
from rest_framework.authtoken.models import Token
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import status

# Create your views here.



class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer

# Register işlemiyle birlikte token oluşturmak istiyorsak 👇

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid(raise_exception=False):
            return Response({"message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        user = serializer.save()
        #token= Token.objects.create(user=user)
        # by signal token 
        token= Token.objects.get(user=user)
        data = serializer.data
        data['token'] = token.key
        data["messages"]="User created successfully "
        headers = self.get_success_headers(serializer.data)
        return Response(data, status=status.HTTP_201_CREATED, headers=headers)


# Yukarıdaki register işlemi ile user created ettiğimizde aşağıda gösterilen bilgiler ve token oluşacaktır.Hepsi required=True olduğundan tüm alanların doldurulması ve email unique olması gerekmektedir.
"""
        {
    "message": "created successfully",
    "details": {
        "username": "Adams",
        "email": "test@gmail.com",
        "first_name": "adams",
        "last_name": "john",
        "token": "43f48227ae01fa3dabfbec59dee3d4905b53b58a234234"
    }
}     
 """


#! FUNCTİON 
@api_view(['POST'])
def logout_view(request):
    if request.method == 'POST':
        request.user.auth_token.delete()
        data = {
            'message': 'logout'
        }
        return Response(data)
