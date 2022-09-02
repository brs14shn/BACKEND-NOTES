from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class  UserProfile(models.Model):
    portfolio = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
     
     #burada auth içinden gelen user modelini kullanıp eşitledik
    def __str__(self):
        return self.user.username
