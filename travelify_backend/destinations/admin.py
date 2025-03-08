from django.contrib import admin
from .models import Destination, Category, SearchHistory

admin.site.register(Destination)
admin.site.register(Category)
admin.site.register(SearchHistory)
