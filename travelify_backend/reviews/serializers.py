from rest_framework import serializers
from .models import Review

class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()  # Show username instead of user ID
    destination = serializers.StringRelatedField()  # Show destination name instead of destination ID

    class Meta:
        model = Review
        fields = ['id', 'user', 'destination', 'rating', 'comment', 'created_at']
