from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import UserSerializer
from rest_framework.decorators import action

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # Custom Action to get user by username
    @action(detail=False, methods=['get'], url_path='username/(?P<username>[^/.]+)')
    def get_user_by_username(self, request, username=None):
        try:
            user = User.objects.get(username=username)
            serializer = self.get_serializer(user)
            return Response(serializer.data)
        except User.DoesNotExist:
            return Response({"detail": "User not found"}, status=status.HTTP_404_NOT_FOUND)

    # Custom Action to change password
    @action(detail=True, methods=['put'], url_path='change-password')
    def change_password(self, request, pk=None):
        user = self.get_object()
        new_password = request.data.get('password')

        if new_password:
            user.set_password(new_password)
            user.save()
            return Response({"detail": "Password updated successfully"})
        return Response({"detail": "Password not provided"}, status=status.HTTP_400_BAD_REQUEST)
