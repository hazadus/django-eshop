from django.db import models
from django.urls import reverse


class Category(models.Model):
    """
    Describes product category in eshop.
    """
    name = models.CharField(verbose_name="Название", max_length=256)
    slug = models.SlugField(max_length=256, unique=True)
    parent_category = models.ForeignKey("self", verbose_name="Родительская категория", on_delete=models.CASCADE,
                                        null=True, blank=True, default=None, related_name="children_categories")

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['name']),
        ]
        verbose_name = "категория"
        verbose_name_plural = "категории"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("shop:product_list_by_category", args=[self.slug])


class Product(models.Model):
    """
    Describes a product for sale in eshop.
    """
    category = models.ForeignKey(Category, related_name="products", on_delete=models.CASCADE, verbose_name="Категория")
    name = models.CharField(verbose_name="Название", max_length=256)
    slug = models.SlugField(max_length=256, unique=True)
    image = models.ImageField(verbose_name="Фото", upload_to="products/%Y/%m/%d", blank=True)
    description = models.TextField(verbose_name="Описание", blank=True)
    # For the price field, we use DecimalField instead of FloatField to avoid rounding issues.
    # NB: always use DecimalField for prices!
    price = models.DecimalField(verbose_name="Цена", max_digits=10, decimal_places=2)
    available = models.BooleanField(verbose_name="Наличие", default=True)
    created = models.DateTimeField(verbose_name="Создан", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Изменён", auto_now=True)

    class Meta:
        ordering = ["name"]
        # Define indices to improve performance for most used queries
        indexes = [
            models.Index(fields=["id", "slug"]),
            models.Index(fields=["name"]),
            models.Index(fields=["-created"]),
        ]
        verbose_name = "товар"
        verbose_name_plural = "товары"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("shop:product_detail", args=[self.id, self.slug])
