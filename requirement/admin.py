from django.contrib import admin
from .models import Requirement

@admin.register(Requirement)
class RequirementAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'state', 'city', 'transaction_type', 'budget', 'contact']
    search_fields = ['title', 'user__username', 'state', 'city']
