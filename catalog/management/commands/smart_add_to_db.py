import json

from django.core.management import BaseCommand

from django.db import connection

from catalog.models import Category, Product


class Command(BaseCommand):

    @staticmethod
    def json_r_products():
        with open("product_data.json", encoding="UTF-8") as file:
            read_data = file.read()
            return json.loads(read_data)

    @staticmethod
    def json_r_categories():
        with open("category_data.json", encoding="UTF-8") as file:
            read_data = file.read()
            return json.loads(read_data)

    def handle(self, *args, **options):

        with connection.cursor() as cursor:

            cursor.execute("ALTER SEQUENCE catalog_category_id_seq RESTART WITH 1")

            cursor.execute("ALTER SEQUENCE catalog_product_id_seq RESTART WITH 1")

        Product.objects.all().delete()
        Category.objects.all().delete()

        product_for_create = []
        category_for_create = []

        for category in Command.json_r_categories():
            category_for_create.append(Category(**category.get("fields", {})))

        Category.objects.bulk_create(category_for_create)

        for product in Command.json_r_products():
            category_pk = product.get("fields", {}).pop("category")
            product_for_create.append(
                Product(
                    category=Category.objects.get(pk=category_pk),
                    **product.get("fields", {})
                )
            )

        Product.objects.bulk_create(product_for_create)
