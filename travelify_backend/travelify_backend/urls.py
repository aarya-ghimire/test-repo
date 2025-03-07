from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('users.urls')),        # User-related APIs
    path('api/', include('destinations.urls')), # Destination-related APIs
    path('api/', include('wishlists.urls')),     # Wishlist-related APIs
]
