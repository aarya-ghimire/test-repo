from rest_framework import viewsets  # Ensure this import is present
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action  # Add this import
from .models import Destination
from .serializers import DestinationSerializer

class DestinationViewSet(viewsets.ModelViewSet):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer

    # Custom Action to filter destinations by region or category
    @action(detail=False, methods=['get'], url_path='filter')
    def filter_destinations(self, request):
        region = request.query_params.get('region')
        category = request.query_params.get('category')
        destinations = Destination.objects.all()

        if region:
            destinations = destinations.filter(region__icontains=region)
        if category:
            destinations = destinations.filter(category__icontains=category)

        serializer = self.get_serializer(destinations, many=True)
        return Response(serializer.data)
