from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from rest_framework import filters
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

from slider.models import Slider
from slider.pagination import ResultsSetPagination
from slider.serializers import SliderSerializer


class SliderListView(ListAPIView):
    search_fields = ['title']
    filter_backends = (filters.SearchFilter,)
    serializer_class = SliderSerializer
    pagination_class = ResultsSetPagination

    def get_queryset(self):
        return Slider.objects.all().order_by('order')


@api_view(['GET'])
def sliderdetail(request, pk):
    slider = get_object_or_404(Slider, pk=pk)
    serializer = SliderSerializer(slider, context={'request': request})
    return Response(serializer.data)
