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

    def update(self, instance, validated_data):  # ✅ Add this update method
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.best_time = validated_data.get('best_time', instance.best_time)
        instance.image_url = validated_data.get('image_url', instance.image_url)
        instance.category = validated_data.get('category', instance.category)
        instance.save()
        return instance
