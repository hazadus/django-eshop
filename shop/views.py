from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponse

from .models import Category, Product


def product_list(request: HttpRequest, category_slug: str = None) -> HttpResponse:
    """
    List all available products in the shop, or all available products in selected category.
    """
    category = None

    categories = Category.objects.all()
    products = Product.objects.filter(available=True)

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    return render(request, "shop/product_list.html", {
        "category": category,
        "categories": categories,
        "products": products
    })


def product_detail(request: HttpRequest, product_id: int, slug: str) -> HttpResponse:
    product = get_object_or_404(Product, id=product_id, slug=slug, available=True)
    return render(request, "shop/product_detail.html", {
        "product": product,
    })
