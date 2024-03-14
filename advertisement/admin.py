from django.contrib import admin
from django.db import models
from django.forms import Textarea
from .models import Advertisement
from deal.models import Deal

@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'title', 'state', 'city', 'transaction_type', 'price', 'contact']
    search_fields = ['title', 'user__username', 'state', 'city']

    # Define the DealInline class inside RequirementAdmin to access it easily
    class DealInline(admin.TabularInline):
        model = Deal
        # You can also specify extra attributes here if needed, for example:
        extra = 0  # This prevents extra empty forms for new objects
        # Customizing the form if necessary, for example, using a larger textarea for text fields:
        formfield_overrides = {
            models.TextField: {'widget': Textarea(attrs={'rows': 1, 'cols': 40})},
        }
        # Specify readonly fields if you want to prevent modification through the inline, for example:
        readonly_fields = ('deal_maker',)
        fields = ('advertisement', 'deal_maker', 'status')  # Adjust this list based on your needs

    # Add the inline to your admin model
    inlines = [DealInline]