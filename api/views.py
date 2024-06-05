from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny

from entrez_api.serializer import SequenceRecordSerializer
from entrez_api.models import SequenceRecord

# Implement registration form, generic view built into django 
class CreateUserView(generics.CreateAPIView):
    # Specify all objects will look up so dont create duplicate
    queryset = User.objects.all()
    serializer_class = UserSerializer # What kind of data to create user
    permission_classes = [AllowAny] # allow anyone to call this

# lists records or creates new one
class SequenceRecordListCreate(generics.ListCreateAPIView):
    serializer_class = SequenceRecordSerializer # Data passed will tell us if valid
    permission_classes = [IsAuthenticated] # Cant call route unless authenticated and pass JWT token

    def get_queryset(self):
        user = self.request.user # Get authenticated user, and use to filter records written by user
        return SequenceRecords.objects.filter(author=user)
    
    def perform_create(self, serializer):
        # Pass serializer and validate, then add any extras that need to manually do
        if(serializer.is_valid()):
            serializer.save(author=self.request.user)
        else: 
            print(serilizer.errors)

class SequenceRecordDelete(generics.DestroyAPIView):
    serializer_class = SequenceRecordSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Only delete records you own
        user = self.request.user
        return SequenceRecord.objects.filter(author=user)