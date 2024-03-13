from rest_framework import serializers
from user.serializers import UserSerializer
from .models import Deal


class DealSerializer(serializers.ModelSerializer):
    deal_maker = UserSerializer(read_only=True)

    class Meta:
        model = Deal
        fields = "__all__"

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret.pop("deal_maker", None)
        return ret
