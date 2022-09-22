from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import RegistrationSerializer
from rest_framework.authtoken.models import Token
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import status


# Create your views here.
# Registration with function based view
# @api_view(['POST'])
# def registration_view(request):
#     if request.method == 'POST':
#         serializer = RegistrationSerializer(data=request.data)
#         data = {}
#         if serializer.is_valid():
#             password = serializer.validated_data.get('password')
#             # serializer.validated_data['password'] = make_password(password)
#             user = serializer.save()
#             user.set_password(password)
#             user.save()
#             # token, _ = Token.objects.get_or_create(user=user)
#             # data = serializer.data
#             # data['token'] = token.key
#         else:
#             data = serializer.errors
#         return Response(data)

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer
    
    #yukarıdaki işlem register için yeterli 
    # aşağıdaki işlemi register olduktan sonra login olması için yaptık

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid(raise_exception=False):
            return Response({"message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        user = serializer.save()
        #token= Token.objects.create(user=user)
        token= Token.objects.get(user=user)
        data = serializer.data
        data['token'] = token.key

        headers = self.get_success_headers(serializer.data)
        return Response({"message": "created successfully", "details": data}, status=status.HTTP_201_CREATED, headers=headers)
  
@api_view(['POST'])
def logout_view(request):
    if request.method == 'POST':
        request.user.auth_token.delete()
        data = {
            'message': 'logout'
        }
        return Response(data)


