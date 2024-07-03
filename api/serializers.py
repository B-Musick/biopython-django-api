from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password", "email"]
        # Accept password when creating user, but dont return when giving data
        extra_kwargs = {"password": {"write_only": True}} 

    def create(self, validated_data):
        # Method called when want to create new version of user
        # Serializer automatically looks at the fields and makes sure valid
        user = User.objects.create_user(**validated_data)
        return user
