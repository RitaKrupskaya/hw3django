# Generated by Django 5.0.6 on 2024-07-18 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0004_product_manufactured_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="description",
            field=models.TextField(
                blank=True,
                help_text="Описание продукта",
                max_length=100,
                null=True,
                verbose_name="Описание",
            ),
        ),
    ]
