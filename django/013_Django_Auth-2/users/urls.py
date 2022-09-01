from django.urls import path

from .views import user_logout

urlpatterns = [
   path('logout/', user_logout, name='logout'),
]