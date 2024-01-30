from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import uuid
from .manager import UserManager


# Create your models here.
class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=16)
    is_verified = models.BooleanField(default=False)
    otp  = models.CharField(max_length=6,null= True, blank=True)
    last_login_time= models.DateTimeField(null = True, blank = True)
    last_logout_time= models.DateTimeField(null = True, blank = True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()
    def name(self):
        return self.first_name + ' ' + self.last_name
    def __str__(self) :
        return self.email
    
