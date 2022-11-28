from django.db import models
from shop.models import Product


class OrderStatus(models.Model):
    """
    Defines a status of order.

    sort_index shows the position of a status in processing pipeline.
    """
    name = models.CharField(verbose_name="Название", max_length=32)
    sort_index = models.IntegerField(verbose_name="Очередность")
    code = models.CharField(verbose_name="Код", max_length=32)

    class Meta:
        ordering = ["sort_index"]
        verbose_name = "статус заказа"
        verbose_name_plural = "статусы заказа"

    def __str__(self):
        return self.name


class Order(models.Model):
    """
    Defines an order made by customer.
    """
    first_name = models.CharField(verbose_name="Имя", max_length=32)
    last_name = models.CharField(verbose_name="Фамилия", max_length=32)
    email = models.EmailField(verbose_name="E-mail")
    address = models.CharField(verbose_name="Адрес", max_length=256)
    postal_code = models.CharField(verbose_name="Почтовый индекс", max_length=6)
    city = models.CharField(verbose_name="Город", max_length=64)
    created = models.DateTimeField(verbose_name="Создан", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Изменён", auto_now=True)
    paid = models.BooleanField(verbose_name="Оплачен", default=False)
    status = models.ForeignKey(OrderStatus, related_name="orders", on_delete=models.CASCADE, verbose_name="Статус")

    class Meta:
        ordering = ["-created"]
        indexes = [
            models.Index(fields=["-created"]),
        ]
        verbose_name = "заказ"
        verbose_name_plural = "заказы"

    def __str__(self):
        return f"Заказ {self.id}"

    def get_total_cost(self):
        """
        Returns total cost of all products in order.
        """
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    """
    Defines one item (row) of the order.
    NB: don't forget to use DecimalField for price field!
    """
    order = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE, verbose_name="Заказ")
    product = models.ForeignKey(Product, related_name="order_items", on_delete=models.CASCADE, verbose_name="Товар")
    price = models.DecimalField(verbose_name="Цена", max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(verbose_name="Количество", default=1)

    def __str__(self):
        return str(self.id)

    def get_cost(self):
        return self.price * self.quantity
