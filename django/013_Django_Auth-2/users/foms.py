from django.contrib.auth.models import User
from .models import UserProfile

from django import forms

from django.contrib.auth.forms import UserCreationForm


class UserForm(UserCreationForm):
    class Meta:
        model=user #user ı kullan ve sadece username ve email aldık
        fields=('username', 'email')

class UserProfileForm(forms.ModelForm):   #burada hazır modelden form ürettik
    class Meta:
        model = UsersProfile
        exclude = ('user',)    #tek elemanlı tupple kullandığımız için sonuna , koyduk
        #! user haricindeki diğer fieldsları getir

