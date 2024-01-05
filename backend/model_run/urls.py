from django.urls import path
from .views import detect_objects

urlpatterns = [
    path('', detect_objects, name='detect_objects'),
]