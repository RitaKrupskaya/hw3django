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
        max_length=100,
        verbose_name="Описание",
        help_text="Описание продукта",
        blank=True,
        null=True,
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
    manufactured_at = models.DateTimeField(
        auto_now=True, verbose_name="Дата производства", blank=True, null=True
    )

    def __str__(self):
        return f"{self.name}: {self.price_for_buy} руб."

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"


class Version(models.Model):
    product = models.ForeignKey(
        Product,
        related_name="versions",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Продукт",
    )
    version_number = models.CharField(
        max_length=10,
        verbose_name="Номер версии",
        help_text="Введите номер версии",
        null=True,
        blank=True,
    )
    version_name = models.CharField(
        max_length=100,
        verbose_name="Название версии",
        help_text="Введите название версии",
        null=True,
        blank=True,
    )
    is_version_active = models.BooleanField(
        default=False,
        verbose_name="Активная версия",
        help_text="Является ли версия активной",
    )

    class Meta:
        verbose_name = "Версия"
        verbose_name_plural = "Версии"
        ordering = ["version_number", "version_name"]

    def __str__(self):
        return self.version_name
