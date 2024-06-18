from django.contrib import admin
from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()

urlpatterns = [
    path('register/', Register.as_view()),
    path('verify/',VerifyOTP.as_view()),
    path('', include(router.urls)),
    path('login/', Login.as_view()),
    path('logout/', Logout.as_view()),
    path('register-hospital/', RegisterHospital.as_view()),
]