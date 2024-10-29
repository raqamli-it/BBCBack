from django.urls import path

from credit_conditions.views import InfoListView, infodetail


urlpatterns = [
    path('info/', InfoListView.as_view(), name='info-list'),
    path('info/<int:pk>/', infodetail, name='info-detail'),
]
