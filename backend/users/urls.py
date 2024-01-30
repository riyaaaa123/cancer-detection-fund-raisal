from django.contrib import admin
from django.urls import path, include
from .views import *
from rest_framework import routers
from .views import HospitalViewSet

router = routers.DefaultRouter()
router.register(r'hospitals', HospitalViewSet)

urlpatterns = [
    path('register/', Register.as_view()),
    path('verify/',VerifyOTP.as_view()),
    path('login/', Login.as_view()),
    path('logout/', Logout.as_view()),
    path('api/', include(router.urls)),
]