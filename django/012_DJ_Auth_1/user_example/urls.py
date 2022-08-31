from django.urls import path, include
from .views import (
    home,
    special
)

urlpatterns = [
    path('', home, name="home"),
    path('special', special, name="special"),
]
