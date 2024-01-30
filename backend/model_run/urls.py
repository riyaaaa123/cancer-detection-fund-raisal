from django.urls import path
from .views import detect_objects
from .views import save_prediction_result

urlpatterns = [
    path('', detect_objects, name='detect_objects'),
    path('api/save_prediction/', save_prediction_result, name='save_prediction_result'),
]