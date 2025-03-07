from django.urls import path
from .views import WishlistViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'wishlist', WishlistViewSet, basename='wishlist')

urlpatterns = router.urls
