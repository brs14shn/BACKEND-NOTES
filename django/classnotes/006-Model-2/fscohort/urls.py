from django.urls import path
from fscohort.views import fscohort,subfolder

urlpatterns = [
    path("",fscohort), # /fscohort/
    path("subfolder/",subfolder) #* /fscohort/subfolder
]