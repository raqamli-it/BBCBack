from django.urls import path

from about.views import TopListView, topdetail, WorkersListView, workersdetail, ServicesListView, servicesdetail

urlpatterns = [
    path('top/', TopListView.as_view(), name='top-list'),
    path('top/<int:pk>/', topdetail, name='top-detail'),

    path('workers/', WorkersListView.as_view(), name='workers-list'),
    path('workers/<int:pk>/', workersdetail, name='workers-detail'),

    path('services/', ServicesListView.as_view(), name='services-list'),
    path('services/<int:pk>/', servicesdetail, name='services-detail'),
]
