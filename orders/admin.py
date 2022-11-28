from django.contrib import admin

from .models import Order, OrderStatus, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


@admin.register(OrderStatus)
class OrderStatusAdmin(admin.ModelAdmin):
    list_display = ["sort_index", "name", "code"]


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["id", "status", "first_name", "last_name", "email",  "city", "address", "postal_code", "paid",
                    "created", "updated"]
    list_filter = ["paid", "created", "updated"]
    inlines = [OrderItemInline]
