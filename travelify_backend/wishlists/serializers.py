from rest_framework import serializers
from .models import Wishlist

class WishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wishlist
        fields = ['id', 'user', 'destination', 'created_at']
from rest_framework import serializers
from .models import Wishlist

class WishlistSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()  # Show username instead of user ID
    destination = serializers.StringRelatedField()  # Show destination name instead of destination ID

    class Meta:
        model = Wishlist
        fields = ['id', 'user', 'destination', 'created_at']
