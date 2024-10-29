from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from rest_framework import filters
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

from credit_conditions.models import Info
from credit_conditions.pagination import ResultsSetPagination
from credit_conditions.serializers import InfoSerializer


class InfoListView(ListAPIView):
    search_fields = ['title']
    filter_backends = (filters.SearchFilter,)
    serializer_class = InfoSerializer
    pagination_class = ResultsSetPagination

    def get_queryset(self):
        return Info.objects.all()


@api_view(['GET'])
def infodetail(request, pk):
    info = get_object_or_404(Info, pk=pk)
    serializer = InfoSerializer(info, context={'request': request})
    return Response(serializer.data)
