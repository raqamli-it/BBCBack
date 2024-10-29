from django.urls import path

from slider.views import SliderListView, sliderdetail

urlpatterns = [
    path('slider/', SliderListView.as_view(), name='slider-list'),
    path('slider/<int:pk>/', sliderdetail, name='slider-detail'),
]
