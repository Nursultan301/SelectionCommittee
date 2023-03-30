from rest_framework import generics, viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser

from api.v1.organization.serializers import EntrantSerializer
from apps.organization.models import Entrant


class EntrantViewSet(viewsets.ModelViewSet):
    model = Entrant
    queryset = model.objects.filter(active=True)
    serializer_class = EntrantSerializer
    permission_classes = [IsAdminUser]

    def get_permissions(self):
        if self.action in ['create']:
            self.permission_classes = [AllowAny]
        return super().get_permissions()
