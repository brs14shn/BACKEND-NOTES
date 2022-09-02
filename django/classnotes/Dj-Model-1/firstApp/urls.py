from django.urls import path
from .views import firstApp

urlpatterns = [
    path("",firstApp),
]