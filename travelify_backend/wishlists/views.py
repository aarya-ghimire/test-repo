from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Wishlist
from .serializers import WishlistSerializer
from rest_framework.decorators import action

class WishlistViewSet(viewsets.ModelViewSet):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer

    # Custom Action to get wishlist by user
    @action(detail=False, methods=['get'], url_path='user/(?P<user_id>[^/.]+)')
    def get_wishlist_by_user(self, request, user_id=None):
        wishlist = Wishlist.objects.filter(user__id=user_id)
        serializer = self.get_serializer(wishlist, many=True)
        return Response(serializer.data)
