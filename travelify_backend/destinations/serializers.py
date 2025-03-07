from rest_framework import serializers
from .models import Category, Destination

class DestinationSerializer(serializers.ModelSerializer):
    category = serializers.CharField(write_only=True)  # Accepts category as a string
    category_data = serializers.SerializerMethodField(read_only=True)  # Returns category details

    class Meta:
        model = Destination
        fields = ['id', 'name', 'description', 'category', 'best_time', 'image_url', 'created_at', 'category_data']
    
    def get_category_data(self, obj):
        return {"id": obj.category.id, "name": obj.category.name}

    def create(self, validated_data):
        category_name = validated_data.pop('category', None)

        if category_name:
            category, created = Category.objects.get_or_create(name=category_name)
            validated_data['category'] = category

        return Destination.objects.create(**validated_data)
