from django.urls import path

from connection.views import LocationListView, locationdetail, ContactListView, contactdetail

urlpatterns = [
    path('location/', LocationListView.as_view(), name='location-list'),
    path('location/<int:pk>/', locationdetail, name='location-detail'),

    path('contact/', ContactListView.as_view(), name='contact-list'),
    path('contact/<int:pk>/', contactdetail, name='contact-detail'),
]
