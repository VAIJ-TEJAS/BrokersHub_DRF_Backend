from django.contrib import admin
from django.utils.html import format_html
from django.db import models
from django.forms import Textarea
from deal.models import Deal
from .models import Requirement

@admin.register(Requirement)
class RequirementAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'title', 'state', 'city', 'area', 'transaction_type', 'budget', 'contact']
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
        
        
        readonly_fields = ('deal_maker', 'deal_maker_phone', 'deal_maker_email', 'status')

        def deal_maker_phone(self, instance):
            # Return the deal_maker's phone number
            return instance.deal_maker.phone
        deal_maker_phone.short_description = 'Deal Maker Phone'

        def deal_maker_email(self, instance):
            # Return the deal_maker's email
            return format_html('<a href="mailto:{}">{}</a>', instance.deal_maker.email, instance.deal_maker.email)
        deal_maker_email.short_description = 'Deal Maker Email'

        fields = ('requirement', 'deal_maker', 'deal_maker_phone', 'deal_maker_email', 'status')

    # Add the inline to your admin model
    inlines = [DealInline]