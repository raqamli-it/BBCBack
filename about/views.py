from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from rest_framework import filters
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

from about.models import Top, Workers, Services
from about.pagination import ResultsSetPagination
from about.serializers import TopSerializer, WorkersSerializer, ServicesSerializer


class TopListView(ListAPIView):
    search_fields = ['title']
    filter_backends = (filters.SearchFilter,)
    serializer_class = TopSerializer
    pagination_class = ResultsSetPagination

    def get_queryset(self):
        return Top.objects.all()


@api_view(['GET'])
def topdetail(request, pk):
    top = get_object_or_404(Top, pk=pk)
    serializer = TopSerializer(top, context={'request': request})
    return Response(serializer.data)


class WorkersListView(ListAPIView):
    search_fields = ['title']
    filter_backends = (filters.SearchFilter,)
    serializer_class = WorkersSerializer
    pagination_class = ResultsSetPagination

    def get_queryset(self):
        return Workers.objects.all()


@api_view(['GET'])
def workersdetail(request, pk):
    workers = get_object_or_404(Workers, pk=pk)
    serializer = WorkersSerializer(workers, context={'request': request})
    return Response(serializer.data)


class ServicesListView(ListAPIView):
    search_fields = ['title']
    filter_backends = (filters.SearchFilter,)
    serializer_class = ServicesSerializer
    pagination_class = ResultsSetPagination

    def get_queryset(self):
        return Services.objects.all()


@api_view(['GET'])
def servicesdetail(request, pk):
    services = get_object_or_404(Services, pk=pk)
    serializer = ServicesSerializer(services, context={'request': request})
    return Response(serializer.data)
