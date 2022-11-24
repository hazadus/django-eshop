from decimal import Decimal
from django.conf import settings
from django.http import HttpRequest

from shop.models import Product


class Cart:
    """
    Describes shopping cart in eshop.
    """
    def __init__(self, request: HttpRequest):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)

        if not cart:
            # Create an empty cart
            cart = self.session[settings.CART_SESSION_ID] = {}

        self.cart = cart

    def add(self, product: Product, quantity: int = 1, override_quantity: bool = False) -> None:
        """
        Add a product to the cart or update it's quantity.

        :param product: the product instance to add or update in the cart.
        :param quantity: optional integer with the product quantity.
        :param override_quantity: indicates whether the quantity needs to be overridden with the given
                                  quantity (True), or whether the quantity has to be added to the existing
                                  quantity (False).
        """
        product_id = str(product.id)

        if product_id not in self.cart:
            self.cart[product_id] = {
                "quantity": 0,
                "price": str(product.price),
            }

        if override_quantity:
            self.cart[product_id]["quantity"] = quantity
        else:
            self.cart[product_id]["quantity"] += quantity

        self.save()

    def save(self):
        """
        Mark the session as "modified" to make sure it gets saved
        """
        self.session.modified = True

    def remove(self, product: Product):
        """
        Remove a product from the cart.

        :param product: product to remove from the cart.
        """
        product_id = str(product.id)

        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        """
        Iterate over the items in the cart and get the products from the database.
        """
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        cart = self.cart.copy()

        # Add database objects to cart
        for product in products:
            cart[str(product.id)]["product"] = product

        # Iterate over the items in the cart, converting prices from str back to decimal
        for item in cart.values():
            item["price"] = Decimal(item["price"])
            item["total_price"] = item["price"] * item["quantity"]
            yield item

    def __len__(self):
        """
        Count all items (i.e., sum all quantities of items) in the cart.
        """
        return sum(item["quantity"] for item in self.cart.values())

    def get_total_price(self):
        """
        Count total price for all items in the cart.
        """
        return sum(Decimal(item["price"]) * item["quantity"] for item in self.cart.values())
