from django.http import HttpRequest, HttpResponse
from django.views.decorators.http import require_POST
from django.shortcuts import render, redirect, get_object_or_404

from .cart import Cart
from shop.models import Product
from .forms import CartAddProductForm


@require_POST
def cart_add(request: HttpRequest, product_id: int) -> HttpResponse:
    """
    View for adding products to the cart or updating quantities for existing products.
    """
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)

    if form.is_valid():
        data = form.cleaned_data
        cart.add(product=product, quantity=data["quantity"], override_quantity=data["override"])

    return redirect("cart:cart_detail")


@require_POST
def cart_remove(request: HttpRequest, product_id) -> HttpResponse:
    """
    View to remove products from the cart.
    """
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product=product)

    return redirect("cart:cart_detail")


def cart_detail(request: HttpRequest) -> HttpResponse:
    cart = Cart(request)

    for item in cart:
        # Create a form for each item in the cart with it's initial quantity
        item["update_quantity_form"] = CartAddProductForm(initial={
            "quantity": item["quantity"],
            "override": True,
        })

    return render(request, "cart/cart_detail.html", {
        "cart": cart,
    })
