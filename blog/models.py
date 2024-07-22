from django.db import models


class Post(models.Model):
    title = models.CharField(
        max_length=150, verbose_name="Заголовок",
    )
    slug = models.SlugField(unique=True, max_length=150, blank=True)
    body = models.TextField(
        verbose_name="Содержание", blank=True, null=True
    )
    image = models.ImageField(
        upload_to="blog/photo",
        verbose_name="Превью",
        blank=True,
        null=True,
    )
    posted_at = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)
    is_published = models.BooleanField(
        default=True, verbose_name="Опубликован",
    )
    view_count = models.IntegerField(default=0, verbose_name="Просмотры")

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
