from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import QueryViewSet

router = DefaultRouter()
router.register(r'userq', QueryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]