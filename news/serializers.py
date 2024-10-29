from rest_framework import serializers

from news.models import News


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('id', 'title_uz', 'title_ru', 'description_uz', 'description_ru', 'image','order', 'created_at',
                  'updated_at',)
