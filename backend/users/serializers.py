from rest_framework import serializers
from .models import User, Hospital
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields= ['email','password','is_verified']
        
class VerifyAccountSerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp = serializers.CharField()
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

        
           

# serializers.py

class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        fields = ['user', 'name', 'phone_number', 'certificate']
