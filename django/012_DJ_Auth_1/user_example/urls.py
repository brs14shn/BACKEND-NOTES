from django.urls import path, include
from .views import (
    home,
    special,
    register
)

urlpatterns = [
    path('', home, name="home"),
    path('special/', special, name="special"),
    path("register/",register,name="register")
]
