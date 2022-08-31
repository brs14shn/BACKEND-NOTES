from django.urls import path, include
from .views import (
    home,
    special,
    register
)
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', home, name="home"),
    path('special/', special, name="special"),
    path("register/",register,name="register"),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name="registration/password_change.html"), name="password_change")
]
