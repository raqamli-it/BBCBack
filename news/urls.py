from django.urls import path

from news.views import NewsListView, newsdetail


urlpatterns = [
    path('news/', NewsListView.as_view(), name='news-list'),
    path('news/<int:pk>/', newsdetail, name='news-detail'),
]
