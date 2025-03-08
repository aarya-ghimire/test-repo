from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Review
from .serializers import ReviewSerializer
from rest_framework.decorators import action

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    # ✅ Get Reviews for a Specific Destination
    @action(detail=False, methods=['get'], url_path='destination/(?P<destination_id>[^/.]+)')
    def get_reviews_for_destination(self, request, destination_id=None):
        reviews = Review.objects.filter(destination__id=destination_id)
        serializer = self.get_serializer(reviews, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # ✅ Get Reviews by a Specific User
    @action(detail=False, methods=['get'], url_path='user/(?P<user_id>[^/.]+)')
    def get_reviews_by_user(self, request, user_id=None):
        reviews = Review.objects.filter(user__id=user_id)
        serializer = self.get_serializer(reviews, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # ✅ Create Review
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # ✅ Update Review
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # ✅ Delete Review
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({"detail": "Review deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
