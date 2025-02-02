from django.core.management.base import BaseCommand
from catalog.models import Product, Category

class Command(BaseCommand):
    help = "Добавляет тестовые продукты в базу"

    def handle(self, *args, **kwargs):
        Product.objects.all().delete()
        Category.objects.all().delete()

        cat1 = Category.objects.create(name="Электроника", description="Гаджеты")
        Product.objects.create(name="Samsung Galaxy", category=cat1, price=700)

        self.stdout.write(self.style.SUCCESS("Тестовые данные загружены!"))
