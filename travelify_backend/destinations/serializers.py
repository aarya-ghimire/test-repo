from rest_framework import serializers
from .models import Category, Destination

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class DestinationSerializer(serializers.ModelSerializer):
    category = CategorySerializer()  # Nested category serializer

    class Meta:
        model = Destination
        fields = ['id', 'name', 'description', 'category', 'best_time', 'image_url', 'created_at']

    def create(self, validated_data):
        # Extract category data from validated data
        category_data = validated_data.pop('category')

        # Create or get the category (to avoid duplicates)
        category, created = Category.objects.get_or_create(name=category_data['name'])

        # Create the destination instance
        destination = Destination.objects.create(category=category, **validated_data)

        return destination
