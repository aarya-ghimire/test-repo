from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Review
from .serializers import ReviewSerializer
from rest_framework.decorators import action

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    # Retrieve Reviews for a Specific Destination
    @action(detail=False, methods=['get'], url_path='destination/(?P<destination_id>[^/.]+)')
    def get_reviews_for_destination(self, request, destination_id=None):
        reviews = Review.objects.filter(destination__id=destination_id)
        serializer = self.get_serializer(reviews, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Retrieve Reviews for a Specific User
    @action(detail=False, methods=['get'], url_path='user/(?P<user_id>[^/.]+)')
    def get_reviews_by_user(self, request, user_id=None):
        reviews = Review.objects.filter(user__id=user_id)
        serializer = self.get_serializer(reviews, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
