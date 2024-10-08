# Generated by Django 4.2.2 on 2024-08-15 16:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0008_alter_product_options_product_is_published"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="product",
            options={
                "ordering": ["name", "category"],
                "permissions": [
                    ("can_cancel_publication", "Can cancel publication of product"),
                    ("can_change_description", "Can change description of product"),
                    ("can_change_category", "Can change category"),
                ],
                "verbose_name": "Продукт",
                "verbose_name_plural": "Продукты",
            },
        ),
    ]
