from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from rest_framework import filters
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

from news.models import News
from news.pagination import ResultsSetPagination
from news.serializers import NewsSerializer


class NewsListView(ListAPIView):
    search_fields = ['title']
    filter_backends = (filters.SearchFilter,)
    serializer_class = NewsSerializer
    pagination_class = ResultsSetPagination

    def get_queryset(self):
        return News.objects.all().order_by('order')


@api_view(['GET'])
def newsdetail(request, pk):
    news = get_object_or_404(News, pk=pk)
    serializer = NewsSerializer(news, context={'request': request})
    return Response(serializer.data)