import json

from django.core.management import BaseCommand

from catalog.models import Category, Product


class Command(BaseCommand):

    @staticmethod
    def json_read():
        with open('catalog.json', encoding='UTF-8') as file:
            return json.load(file)

    def handle(self, *args, **options):

        Category.objects.all().delete()
        Product.objects.all().delete()

        product_for_create = []
        category_for_create = []

        for category in Command.json_read():
            if category['model'] == 'catalog.category':
                category_for_create.append(
                    Category(pk=category['pk'], title=category['fields']['title'], desk=category['fields']['desk'])
                )

        Category.objects.bulk_create(category_for_create)

        for product in Command.json_read():
            if product['model'] == 'catalog.product':
                product_for_create.append(
                    Product(title=product['fields']['title'], desk=product['fields']['desk'],
                            image=product['fields']['image'],

                            category=Category.objects.get(pk=product['fields']['category']),
                            price=product['fields']['price_for_buy'], created_at=product['fields']['created_at'],
                            updated_at=product['fields']['updated_at'])
                )

        Product.objects.bulk_create(product_for_create)
