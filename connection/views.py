from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from rest_framework import filters
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

from connection.models import Location, Contact
from connection.pagination import ResultsSetPagination
from connection.serializers import LocationSerializer, ContactSerializer


class LocationListView(ListAPIView):
    search_fields = ['location']
    filter_backends = (filters.SearchFilter,)
    serializer_class = LocationSerializer
    pagination_class = ResultsSetPagination

    def get_queryset(self):
        return Location.objects.all()


@api_view(['GET'])
def locationdetail(request, pk):
    location = get_object_or_404(Location, pk=pk)
    serializer = LocationSerializer(location, context={'request': request})
    return Response(serializer.data)


class ContactListView(ListAPIView):
    search_fields = ['location']
    filter_backends = (filters.SearchFilter,)
    serializer_class = ContactSerializer
    pagination_class = ResultsSetPagination

    def get_queryset(self):
        return Contact.objects.all()


@api_view(['GET'])
def contactdetail(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    serializer = ContactSerializer(contact, context={'request': request})
    return Response(serializer.data)