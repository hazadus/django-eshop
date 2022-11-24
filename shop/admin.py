from django.contrib import admin

from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "slug"]
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "price", "available", "category", "created", "updated", "slug"]
    list_filter = ["available", "created", "updated"]
    # Fields that can be edited from the list display page of admin section:
    list_editable = ["price", "available"]
    prepopulated_fields = {"slug": ("name",)}
