from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "phone",
            "password",
            "my_referral_code",
            "other_referral_code",
            "state",
            "city",
        ]
        read_only_fields = ["referral_code"]
        extra_kwargs = {"password": {"write_only": True, "required": True}}
