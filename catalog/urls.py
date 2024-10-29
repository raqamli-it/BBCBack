from django.urls import path

from catalog.views import LogoListView, logodetail, CarListView, cardetail, InstallmentPlanListView, \
    installmentplandetail

urlpatterns = [
    path('logo/', LogoListView.as_view(), name='logo-list'),
    path('logo/<int:pk>/', logodetail, name='logo-detail'),

    path('car/', CarListView.as_view(), name='car-list'),
    path('car/<int:pk>/', cardetail, name='car-detail'),

    path('installmentplan/', InstallmentPlanListView.as_view(), name='installmentplan-list'),
    path('installmentplan/<int:pk>/', installmentplandetail, name='installmentplan-detail'),
]
