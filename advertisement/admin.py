from django.contrib import admin
from .models import Advertisement

@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'state', 'city', 'transaction_type', 'price', 'contact']
    search_fields = ['title', 'user__username', 'state', 'city']
