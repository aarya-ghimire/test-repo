from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Wishlist
from .serializers import WishlistSerializer

class WishlistViewSet(viewsets.ModelViewSet):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer

    def create(self, request):
        """Prevent duplicate wishlist entries."""
        user = request.data.get('user')
        destination = request.data.get('destination')

        if Wishlist.objects.filter(user=user, destination=destination).exists():
            return Response({"detail": "Destination already in wishlist"}, status=status.HTTP_400_BAD_REQUEST)

        return super().create(request)
