from django.db import models
import uuid
from django.contrib.auth.hashers import make_password  # ✅ Import

class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=50)  
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=255)  # ✅ Store hashed password
    user_type = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        """Ensure password is hashed before saving."""
        self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username
