from django.db import models


class Category(models.Model):
    name = models.CharField(
        max_length=50, verbose_name="Название", help_text="Название категории"
    )
    description = models.TextField(
        verbose_name="Описание", help_text="Описание категории", blank=True, null=True
    )

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Product(models.Model):
    name = models.CharField(
        max_length=50, verbose_name="Название", help_text="Название продукта"
    )
    description = models.TextField(
        verbose_name="Описание", help_text="Описание продукта", blank=True, null=True
    )
    image = models.ImageField(
        upload_to="catalog/photo",
        verbose_name="Фото",
        help_text="Фото продукта",
        blank=True,
        null=True,
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        verbose_name="Категория",
        related_name="products",
        blank=True,
        null=True,
    )
    price_for_buy = models.IntegerField(
        verbose_name="Цена за покупку", help_text="Цена за покупку продукта"
    )
    created_at = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)
    updated_at = models.DateTimeField(
        verbose_name="Дата последнего изменения", auto_now=True
    )
    manufactured_at = models.DateTimeField(verbose_name='Дата производства', auto_now=True)

    def __str__(self):
        return f"{self.name}: {self.price_for_buy} руб."

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
