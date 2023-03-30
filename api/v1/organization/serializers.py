from rest_framework import serializers

from apps.organization.models import Entrant


class EntrantSerializer(serializers.ModelSerializer):
    """ Список абитуриентов """
    classing = serializers.CharField(source='get_classing_display')

    class Meta:
        model = Entrant
        exclude = ('active',)
