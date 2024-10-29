from rest_framework import serializers

from credit_conditions.models import Info


class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Info
        fields = ('id', 'title_uz', 'title_ru', 'description_uz', 'description_ru', 'file', 'created_at', 'updated_at',)
