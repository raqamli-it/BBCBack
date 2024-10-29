from rest_framework import serializers

from slider.models import Slider


class SliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slider
        fields = ('id', 'title_uz', 'title_ru', 'description_uz', 'description_ru', 'image', 'order', 'created_at',
                  'updated_at',)
