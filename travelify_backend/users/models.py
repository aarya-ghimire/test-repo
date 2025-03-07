from django.db import models
import uuid

class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=50)  
    email = models.EmailField(max_length=100, unique=True)  # Email remains unique
    password = models.CharField(max_length=255)
    user_type = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
