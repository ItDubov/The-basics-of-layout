from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (
    HomePageView, ContactPageView, ProductDetailView,
    ProductCreateView, ProductUpdateView, ProductDeleteView,
    ProductListView
)

app_name = 'products'  # Добавляем пространство имен

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('contacts/', ContactPageView.as_view(), name='contacts'),

    # Просмотр деталей продукта
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),

    # Список всех продуктов
    path('products/', ProductListView.as_view(), name='product_list'),

    # Создание нового продукта
    path('product/create/', ProductCreateView.as_view(), name='product_create'),

    # Редактирование существующего продукта
    path('product/<int:pk>/edit/', ProductUpdateView.as_view(), name='product_edit'),

    # Удаление продукта
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
]

# Подключаем обработку медиафайлов
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
