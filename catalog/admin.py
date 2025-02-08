from django.contrib import admin
from .models import Product, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name', 'description')
    list_filter = ('name',)  # Фильтрация по имени категории

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "is_published")  # Покажем статус публикации
    list_editable = ("is_published",)  # Разрешаем редактирование прямо в списке товаров
    search_fields = ("name", "description")
    list_filter = ("is_published",)  # Фильтрация по статусу публикации
