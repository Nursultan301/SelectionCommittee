from rest_framework import generics, viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser

from api.v1.organization.serializers import EntrantSerializer, SpecialtySerializer
from apps.organization.models import Entrant, Specialty


class BaseViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]

    def get_permissions(self):
        if self.action in ['create']:
            self.permission_classes = [AllowAny]
        return super().get_permissions()


class EntrantViewSet(BaseViewSet):
    queryset = Entrant.objects.all()
    serializer_class = EntrantSerializer


class SpecialtyViewSet(BaseViewSet):
    queryset = Specialty.objects.all()
    serializer_class = SpecialtySerializer
