from django.contrib import admin
from .models import Deal

@admin.register(Deal)
class DealAdmin(admin.ModelAdmin):
    list_display = ['id', 'requirement', 'advertisement', 'deal_maker', 'status']
    list_filter = ['status', 'deal_maker']
    search_fields = ['requirement__title', 'advertisement__title', 'deal_maker__username']
