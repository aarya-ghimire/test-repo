from django.db import models
import uuid
from users.models import User
from destinations.models import Destination

class Wishlist(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'destination')

    def __str__(self):
        return f"{self.user.username} - {self.destination.name}"
