
# Permission (view bazlı)
Authenticated (Kimlik Doğrulama)  and Permission (İzinleri tanımlama)

AllowAny : kısıtlama yok
IsAuthenticated : user kayıtlı ise işlemleri yapıyor
IsAdminUser : admin user için izin veriyor diğerlerine izin vermiyor.
IsAuthenticatedOrReadOnly : auth ise post put delete, değilse sadece get,head,option

   #! IsAuthenticated 👉 A user who is not logged in cannot make get and post requests.
    #! IsAdminUser 👉 Only an admin user can make a get and post requests.
    #! IsAuthenticatedOrReadOnly 👉 If the user is not logged in, he/she can only make a get request.


DjangoModelPermissions :admin panelde verilen user ve grup yetkilerine göre kısıtlama yapıyor

DjangoModelPermissionsOrAnonReadOnly : auth ise djangomodelpermissons uygula değilse read uygula

# DjangoObjectPermissions


# Custom permissions


# Authenticated  (Global bazlı best practice)

* BasicAuthentication

her istekte username ve password istiyor.

Genellikle test için daha uygundur.

güvenli olmayan ve tercih edilmeyn yöntem

settings.py da basic auth için de methodu tanımladık, viewsde ilgili permission yetkisi veriyoruz

settings.py
REST_FRAMEWORK = {   
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication'  
    ]
}


* SessionAuthentication
* TokenAuthentication