# Generated by Django 4.2.2 on 2024-08-15 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0007_product_owner"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="product",
            options={
                "permissions": [
                    ("can_cancel_publication", "Can cancel publication of product"),
                    ("can_change_description", "Can change description of product"),
                    ("can_change_category", "Can change category"),
                ],
                "verbose_name": "Продукт",
                "verbose_name_plural": "Продукты",
            },
        ),
        migrations.AddField(
            model_name="product",
            name="is_published",
            field=models.BooleanField(
                default=False,
                help_text="Опубликовать продукт",
                verbose_name="Опубликовано",
            ),
        ),
    ]