from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from .emails import *
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
                  'status':400,
                  'message': 'wrong otp',
                  'data': 'enter the correct otp',
            
                 })
                user = user.first()
                user.is_verified = True
                user.save()
                return Response({
                  'status':200,
                  'message': 'correct otp',
                  'data': 'registered successfully',
            
                 })
        
            
        except Exception as e:
            print(e)    

            
class HospitalViewSet(viewsets.ModelViewSet):
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializer
    permission_classes = [IsAuthenticated]