from rest_framework import serializers

from apps.organization.models import Entrant


class EntrantListSerializer(serializers.ModelSerializer):
    """ Список абитуриентов """
    grades = serializers.CharField(source='get_grades_display')

    class Meta:
        model = Entrant
        fields = ('first_name', 'last_name', 'full_name', 'photo', 'grades', 'active')


class EntrantDetailSerializer(serializers.ModelSerializer):
    """ Полное информация абитуриента """
    grades = serializers.CharField(source='get_grades_display')
    gender = serializers.CharField(source='get_gender_display')

    class Meta:
        model = Entrant
        exclude = ('active',)
