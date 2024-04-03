from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Deal
from .serializers import DealSerializer


class DealViewSet(viewsets.ModelViewSet):
    queryset = Deal.objects.all()
    serializer_class = DealSerializer

    def create(self, request, *args, **kwargs):
        deal_maker = request.user
        requirement_id = request.data.get('requirement')
        advertisement_id = request.data.get('advertisement')

        existing_deal = Deal.objects.filter(
            deal_maker=deal_maker,
            requirement_id=requirement_id if requirement_id else None,
            advertisement_id=advertisement_id if advertisement_id else None
        ).exclude(requirement__isnull=True, advertisement__isnull=True).exists()

        if existing_deal:
            return Response({"message": "You have already applied for this deal."}, status=status.HTTP_400_BAD_REQUEST)

        return super(DealViewSet, self).create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(deal_maker=self.request.user)
