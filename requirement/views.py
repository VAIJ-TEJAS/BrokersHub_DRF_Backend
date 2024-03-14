from rest_framework import viewsets, permissions
from .models import Requirement
from .serializers import RequirementSerializer


class RequirementViewSet(viewsets.ModelViewSet):
    queryset = Requirement.objects.all()
    serializer_class = RequirementSerializer

    def get_permissions(self):
        if self.request.method == "GET":
            self.permission_classes = [permissions.AllowAny]
        else:
            self.permission_classes = [permissions.IsAuthenticated]
        return super(RequirementViewSet, self).get_permissions()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class MyRequirementViewSet(viewsets.ModelViewSet):
    queryset = Requirement.objects.all()
    serializer_class = RequirementSerializer

    def get_queryset(self):
        return Requirement.objects.filter(user=self.request.user)
