from rest_framework import serializers
from user.serializers import UserSerializer
from .models import Advertisement


class AdvertisementSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Advertisement
        fields = "__all__"

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret.pop("user", None)
        return ret
