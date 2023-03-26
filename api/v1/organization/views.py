from rest_framework import generics, viewsets

from api.v1.organization.serializers import EntrantListSerializer, EntrantDetailSerializer
from apps.organization.models import Entrant


class EntrantViewSet(viewsets.ReadOnlyModelViewSet):
    def get_queryset(self):
        return Entrant.objects.filter(active=True)

    def get_serializer_class(self):
        if self.action == 'list':
            return EntrantListSerializer
        elif self.action == 'retrieve':
            return EntrantDetailSerializer

