from django import forms
from .models import Student


# class StudentForm(forms.Form):
#     first_name = forms.CharField(max_length=50)
#     last_name = forms.CharField(max_length=50)
#     number = forms.IntegerField(required=False)
#     profile_image = forms.ImageField(required=False)

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["first_name", "last_name",
                  "number", "profile_pic"]  #  "__all__"
        labels = {"first_name": "Name"}
