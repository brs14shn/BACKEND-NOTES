from django.urls import path
from .views import home, todo_create, todo_update, todo_delete

urlpatterns = [
    path("", home, name="home"),
    path("add/", todo_create, name="add"),
    path("update/<int:id>", todo_update, name="update"),
    path("delete/<int:id>", todo_delete, name="delete"),
]
