from rest_framework import serializers

from about.models import Top, Workers, Social, Services


class TopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Top
        fields = ('id', 'title_uz', 'title_ru', 'description_uz', 'description_ru', 'image', 'created_at',
                  'updated_at',)


class SocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Social
        fields = ('id', 'social_name', 'link')


class WorkersSerializer(serializers.ModelSerializer):
    socials = SocialSerializer(many=True, read_only=True)

    class Meta:
        model = Workers
        fields = ('id', 'name_uz', 'name_ru', 'position_uz', 'position_ru', 'image', 'socials', 'created_at',
                  'updated_at')


class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = ('id', 'title_uz', 'title_ru', 'description_uz', 'description_ru', 'svg_icon', 'created_at',
                  'updated_at',)
