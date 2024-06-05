from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny

# Implement registration form, generic view built into django 
class CreateUserView(generics.CreateAPIView):
    # Specify all objects will look up so dont create duplicate
    queryset = User.objects.all()
    serializer_class = UserSerializer # What kind of data to create user
    permission_classes = [AllowAny] # allow anyone to call this
