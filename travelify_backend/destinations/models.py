from django.db import models
from users.models import User  # Import User model

class Category(models.Model):
    id = models.AutoField(primary_key=True)  # Auto-incrementing ID
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Destination(models.Model):
    id = models.AutoField(primary_key=True)  # Auto-incrementing ID
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    best_time = models.CharField(max_length=50, blank=True, null=True)
    image = models.ImageField(upload_to='destination_images/', blank=True, null=True)  # Image upload field
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class SearchHistory(models.Model):
    id = models.AutoField(primary_key=True)  # Auto-incrementing ID
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    query = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.query}"
