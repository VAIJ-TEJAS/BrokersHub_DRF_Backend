from rest_framework import serializers
from user.serializers import UserSerializer
from .models import Requirement


class RequirementSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Requirement
        fields = "__all__"

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret.pop("user", None)
        return ret
