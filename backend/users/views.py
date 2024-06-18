from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from .emails import *
from rest_framework.permissions import AllowAny
from django.contrib.auth import login
from django.contrib.auth import logout

from django.views import View
from django.shortcuts import render, redirect
from rest_framework import status
from rest_framework import viewsets
from .models import Hospital
from .serializers import HospitalSerializer
from rest_framework.permissions import IsAuthenticated


class Register(APIView):
    def post(self,request):
      try:
        data=request.data
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            send_otp(serializer.data['email'])
            return Response({
                'status':200,
                'message': 'registration successful, check email',
                'data': serializer.data,
                
            })
        return Response({
            'status':400,
            'message': 'something went wrong',
            'data': serializer.errors,
            
        })
      except Exception as e:
        print(e)

class Login(APIView):
    def post(self, request):
        try:
            serializer = LoginSerializer(data=request.data)

            if serializer.is_valid():
                email = serializer.validated_data['email']
                password = serializer.validated_data['password']

                user = User.objects.filter(email=email).first()

                if user is not None and user.check_password(password):
                    login(request, user)
                    return Response({
                        'status': 200,
                        'message': 'Login successful',
                        'data': {'user_id': user.id, 'email': user.email},
                    })
                else:
                    return Response({
                        'status': 401,
                        'message': 'Invalid email or password',
                    })

            return Response({
                'status': 400,
                'message': 'Invalid input data',
                'data': serializer.errors,
            })

        except Exception as e:
            print(f"Exception during login: {e}")
            return Response({
                'status': 500,
                'message': 'Internal server error',
            })         
class VerifyOTP(APIView):
    def post(self, request):
        try:
            data= request.data
            serializer = VerifyAccountSerializer(data= data)
            if serializer.is_valid():
                email = serializer.data['email']
                otp = serializer.data['otp']
                user= User.objects.filter(email=email)
                if not user.exists():
                  return Response({
                   'status':400,
                   'message': 'something wrong',
                   'data':'invalid email'
                })
                 
                if user[0].otp !=otp:
                  return Response({
                  'status':401,
                  'message': 'wrong otp',
                  'data': 'enter the correct otp',
            
                 })
                user = user.first()
                user.is_verified = True
                user.save()
                login(request,user)
                return Response({
                  'status':200,
                  'message': 'correct otp',
                  'data': 'registered successfully',
                 })
        except Exception as e:
            print(e)           

class Logout(APIView):
    def post(self, request):
        try:
            logout(request)
            return Response({'message': 'Logout successful'})
        except Exception as e:
            return Response({'error': 'Logout failed'})
            print(e)    

            
# class HospitalViewSet(viewsets.ModelViewSet):
#     queryset = Hospital.objects.all()
#     serializer_class = HospitalSerializer

class RegisterHospital(APIView):
    print("HEHEHEHEHEHE")
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            data = request.data
            data['user'] = request.user.id  # Attach the current user to the hospital data
            serializer = HospitalSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'status': 200,
                    'message': 'Hospital registration successful',
                    'data': serializer.data,
                })
            return Response({
                'status': 400,
                'message': 'Something went wrong',
                'data': serializer.errors,
            })
        except Exception as e:
            print(e)
            return Response({
                'status': 500,
                'message': 'Internal server error',
            })