from rest_framework import serializers

from apps.organization.models import Entrant, Specialty


class EntrantSerializer(serializers.ModelSerializer):
    """ Список абитуриентов """
    area = serializers.CharField(source='get_area_display')
    base_class = serializers.CharField(source='get_base_class_display')
    nationality = serializers.CharField(source='get_nationality_display')
    gender = serializers.CharField(source='get_gender_display')
    form_training = serializers.CharField(source='get_form_training_display')
    basic_training = serializers.CharField(source='get_basic_training_display')
    status = serializers.CharField(source='get_status_display')

    class Meta:
        model = Entrant
        fields = "__all__"


class SpecialtySerializer(serializers.ModelSerializer):
    form_training = serializers.CharField(source='get_form_training_display')
    basic_training = serializers.CharField(source='get_basic_training_display')

    class Meta:
        model = Specialty
        fields = "__all__"
