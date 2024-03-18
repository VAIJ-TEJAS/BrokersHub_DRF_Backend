from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    model = User
    fieldsets = UserAdmin.fieldsets + (
        (
            None,
            {
                "fields": (
                    "my_referral_code",
                    "other_referral_code",
                    "state",
                    "city",
                    "phone",
                )
            },
        ),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            None,
            {
                "fields": (
                    "my_referral_code",
                    "other_referral_code",
                    "state",
                    "city",
                    "phone",
                )
            },
        ),
    )
