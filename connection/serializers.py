from rest_framework import serializers

from connection.models import Location, Contact


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('id', 'location', 'lat', 'long', 'created_at', 'updated_at',)


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('id', 'phone', 'email', 'telegram', 'instagram', 'facebook', 'created_at', 'updated_at',)
