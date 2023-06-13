from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class USER(AbstractUser):
    #id=models.IntegerField(auto_created=True,primary_key=True)
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    email=models.EmailField(unique=True)
    is_staff=models.BooleanField(default=False)
    is_admin=models.BooleanField(default=False)

    def __str__(self):
        return self.email

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['username']
    

class Info(models.Model):
    user=models.ForeignKey(USER,on_delete=models.CASCADE)
    Time_logged=models.DateTimeField(auto_now_add=False)
    Time_logged_out=models.DateTimeField(auto_now_add=False,blank=True,null=True,default=None)