
# 1-PERMİSSİONS

#### Authentication (Kimlik kontrolü-yetki kontrolü)

#### Permission (Gerekli izinlerin olup olmadığını tespit eder.)


#! IsAuthenticated 👉 A user who is not logged in cannot make get and post requests.

#! IsAdminUser 👉 Only an admin user can make a get and post requests.

#! IsAuthenticatedOrReadOnly 👉 If the user is not logged in, he/she can only make a get request.

Permission global,view bazlı ve object bazlı tanımlayabiliriz.

- Global olarak;

```

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ]
}
```

- View bazlı permissions:

```
#! CBF
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

class ExampleView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        content = {
            'status': 'request was permitted'
        }
        return Response(content)


from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

#! FBV
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def example_view(request, format=None):
    content = {
        'status': 'request was permitted'
    }
    return Response(content)

```

### PERMİSSİONS

- AllowAny 👉 Herkese izin ver.
İsteğin doğrulanmış veya doğrulanmamış olmasına bakılmaksızın sınırsız erişime izin verir.
 permission_classes = [AllowAny]

- IsAuthenticated
IsAuthenticated izin sınıfı, kimliği doğrulanmamış herhangi bir kullanıcının iznini reddedecek

- IsAdminUser
user.is_staff True olmadığı sürece herhangi bir kullanıcının iznini reddeder ve bu durumda izne izin verilir.

- IsAuthenticatedOrReadOnly
Kimliği doğrulanmış kullanıcıların herhangi bir isteği gerçekleştirmesine izin verir. Yetkisiz kullanıcılara yönelik isteklere, yalnızca istek yönteminin "güvenli" yöntemlerden biri olması durumunda izin verilecektir; GET, HEAD veya OPTİON.

- DjangoModelPermissions
model seviyesinde permission işlemi yapar...

### CUSTOM PERMİSSİONS

VİEW:

```
.has_permission(self, request, view)

if request.method in permissions.SAFE_METHODS:
    # Check permissions for read-only request
else:
    # Check permissions for write request
```

OBJECT:

```
.has_object_permission(self, request, view, obj)

```

**Not1:Permission genellikle view bazlı kurmak best pratice**




# 2-Authentication

- Global olarak ;

settings.py👇
```
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ]
}
```

views.py👇
```
#CBV

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

class ExampleView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        content = {
            'user': str(request.user),  # `django.contrib.auth.User` instance.
            'auth': str(request.auth),  # None
        }
        return Response(content)

#FBV

@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def example_view(request, format=None):
    content = {
        'user': str(request.user),  # `django.contrib.auth.User` instance.
        'auth': str(request.auth),  # None
    }
    return Response(content)
```


Not2 Authentication işlemlerini global olarak kurmak best praticedir.

- BasicAuthentication
 - Yalnızca test için uygundur
 - Kullancının her istekte username ve password olarak kimlik doğrulama işlemi yapar.
 - Güvenli olarak görülmez.
 postmanda bulunan Header> Authorization bulunan base64 koduyla şifrelenmiş bölümü Basic kısmından sonraki kısım; onu alıp base64 decode kontrol eden bir siteye yapıştırdığımızda password ve username
 bilgileri gözükecektir.
 [Base64 kontrol için tıklayınız](https://www.base64decode.org/)



- TokenAuthentication

Kullanmak istiyorsak;

settings.py 👇

```
INSTALLED_APPS = [
    ...
    'rest_framework.authtoken'
]

```

BU İŞLEMİ POSTMAN ÜZERİNDEN TEST ETTİK.
http://127.0.0.1:8000/api/student/ url get,post işlemlerini herkes yapabiliyor.

settings.py

```
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
       
    ]
}
```
global olarak ekledik.

views.py 

```
from rest_framework.permissions import IsAuthenticated


class StudentList(generics.ListCreateAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
    permission_classes = [IsAuthenticated]
    # Artık öğrenci bilgilerimi sadece login olan kullanıcılar görebilirler...
    hata olarak; 👇
    Error: {
    "detail": "Authentication credentials were not provided."
    }  

    Login olmak için POSTMAN DE Auth > sekmesinin altındaki Basic Auth seçtiğimizde 
    username: ***** , password : **** gelecektir.Artık get işlemi yaparsam tüm kullanıcılarıma erişebilirim.
    
   # Herhangi bir permission tanımlaması yapmadığımız için içeriğine erişebiliriz.
class StudentOperations(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()

    http://127.0.0.1:8000/api/student/1 istek gelir.
```
# Buraya kadar basic authentication işlemini yaptık 👆

## TokenAuthentication
Kullanmak için;
settings.py
```
INSTALLED_APPS = [
    ...
    'rest_framework.authtoken'

    ]

    REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
        
    ]
}

```
Bu işlemden sonra 3 adet migrate edilmemiş gelecek tokenları tabloma kaydetmek için ptyhon manage.py migrate komutunu çalıştırmam gerekecek.Bu işlemden sonra admin panelde Auth Token görülecektir.
Tokens sekmesi üzerinden istediğimiz kullanıcı için token üretebilirim.Üretikten sonra postman aracılığıyla test edebilirm.
Postman > Header > kısmında👇

**KEY:** Authorization karşısına ise **VALUE:** Token 34235434ldfhbf35354353 eklenir.
Ama admin panelinden değilde;istek attığımızda token döndürmek istiyorsak bununla ilgili yapmamız gerekn token create etmektir.
Bununla ilgili olarak;

By using signals:
```
# Her kullanıcının otomatik olarak oluşturulmuş generated tokena sahip olmasını istiyorsak, Kullanıcının post_save sinyalini kolayca yakalayabilirsiniz.User create edildiğinde dinliyerek token create ediyor.İnstance dinlenen kısım;Tetikle!!!

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
```

By exposing an api endpoint

```
from rest_framework.authtoken import views
urlpatterns += [
    path('api-token-auth/', views.obtain_auth_token)
]

# istek gönderildiğinde;
{ 'token' : '9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b' } üretecektir.
```
Bunu yapmadan önce login-register işlemleri için user app oluşturuyoruz.main url user url eklemeyi unutma!!!

go to user_api urls.py

```python
from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path
from .views import  logout_view, RegisterView # ,registration_view

urlpatterns = [
    path('login/', obtain_auth_token, name='login'),
    # obtain_auth_token token tablosunda token varsa döndürüyor  
    # yoksa create ediyor.
    # path('register/', registration_view, name='register'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', logout_view, name='logout'),
]
```
login işleminin endpointtine POST isteği gönderildiğinde token created edecek;
http://127.0.0.1:8000/user/login/ endpointine POST işlemi göndermem gerekecek body kısmında username ve password tanımlıyorum.

{
        "username": "barıs",
        "password": "243534534!"      
}
userın tokeni yoksa token oluşturacak varsa onu döndürecek.
Logout olduğunda ise token silinecek.

##  Register işlemi için ve registerdeki bilgileri pythondan json veri tipine çevirmesi için serializers tanımlıyoruz

serializers.py 👇
```
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


class RegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )

        
        user.set_password(validated_data['password'])
        user.save()

        return user

# 2.yöntem model serialzers
# from django.contrib.auth.models import User
# from rest_framework import serializers


# class RegistrationSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password']

```

Register views.py 👇

```
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import RegistrationSerializer
from rest_framework.authtoken.models import Token
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import status

# Create your views here.

from .serializers import RegistrationSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer

""" 

{
    "username": "Adams1",
    "email": "test@gmail1.com",
    "first_name": "adams1",
    "last_name": "john1"
}


"""
# Register işlemiyle birlikte token oluşturmak istiyorsak 👇

    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     if not serializer.is_valid(raise_exception=False):
    #         return Response({"message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    #     user = serializer.save()
    #     token= Token.objects.create(user=user)
    #     data = serializer.data
    #     data['token'] = token.key
    #     headers = self.get_success_headers(serializer.data)
    #     return Response({"message": "created successfully", "details": data}, status=status.HTTP_201_CREATED, headers=headers)


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

```

By using signals ile token create etmek istiyorsam:

models.py 

```

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

komutları giriyorum.

Token create ettiği için views.py bulunan kısmına aşağıdaki gibi değiştiriyorum.
token= Token.objects.get(user=user)



```

## LOGOUT
```
#! FUNCTİON 
@api_view(['POST'])
def logout_view(request):
    if request.method == 'POST':
        request.user.auth_token.delete()
        data = {
            'message': 'logout'
        }
        return Response(data)
```
