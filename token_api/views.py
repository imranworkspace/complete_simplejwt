from django.shortcuts import render

# Create your views here.]
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAdminUser
from rest_framework import viewsets
from .serializers import StudentSerializers
from .models import StudentModel

class StudentModelView(viewsets.ModelViewSet):
    queryset=StudentModel.objects.all()
    serializer_class = StudentSerializers
    # authentication_classes=[JWTAuthentication]
    # permission_classes = [IsAdminUser]
