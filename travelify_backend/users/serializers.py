from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'user_type', 'created_at']
        extra_kwargs = {'password': {'write_only': True}}  # Hide password in responses
from rest_framework import serializers
from .models import User
from django.contrib.auth.hashers import make_password  # Import password hashing utility

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  # Hide password in responses

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'user_type', 'created_at']
        extra_kwargs = {'password': {'write_only': True}}  # Ensure password is write-only

    def create(self, validated_data):
        # Hash the password before saving the user
        password = validated_data.pop('password')
        validated_data['password'] = make_password(password)
        return super().create(validated_data)
