from django.urls import path, include
from .views import HomePageView, ContactPageView, ProductDetailView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('contacts/', ContactPageView.as_view(), name='contacts'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
]
