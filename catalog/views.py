from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from rest_framework import filters
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

from catalog.models import Logo, Car, InstallmentPlan
from catalog.pagination import ResultsSetPagination
from catalog.serializers import LogoSerializer, CarSerializer, InstallmentPlanSerializer


class LogoListView(ListAPIView):
    search_fields = ['title']
    filter_backends = (filters.SearchFilter,)
    serializer_class = LogoSerializer
    pagination_class = ResultsSetPagination

    def get_queryset(self):
        return Logo.objects.all().order_by('order')


@api_view(['GET'])
def logodetail(request, pk):
    logo = get_object_or_404(Logo, pk=pk)
    serializer = LogoSerializer(logo, context={'request': request})
    return Response(serializer.data)


class CarListView(ListAPIView):
    search_fields = ['title']
    filter_backends = (filters.SearchFilter,)
    serializer_class = CarSerializer
    pagination_class = ResultsSetPagination

    def get_queryset(self):
        return Car.objects.all().order_by('order')


@api_view(['GET'])
def cardetail(request, pk):
    car = get_object_or_404(Car, pk=pk)
    serializer = CarSerializer(car, context={'request': request})
    return Response(serializer.data)


class InstallmentPlanListView(ListAPIView):
    search_fields = ['car__title']
    filter_backends = (filters.SearchFilter,)
    serializer_class = InstallmentPlanSerializer
    pagination_class = ResultsSetPagination

    def get_queryset(self):
        return InstallmentPlan.objects.all()


@api_view(['GET'])
def installmentplandetail(request, pk):
    installmentplan = get_object_or_404(InstallmentPlan, pk=pk)
    serializer = InstallmentPlanSerializer(installmentplan, context={'request': request})
    return Response(serializer.data)
