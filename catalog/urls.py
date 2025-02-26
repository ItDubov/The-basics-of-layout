from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import HomePageView, ContactPageView, ProductDetailView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('contacts/', ContactPageView.as_view(), name='contacts'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
]

# Подключаем обработку медиафайлов
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
