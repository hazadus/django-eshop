"""
Contains context processor to put Cart into context.

More on built-in context processors:
https://docs.djangoproject.com/en/4.1/ref/templates/api/#built-in-template-context-processors
"""
from django.http import HttpRequest

from .cart import Cart


def cart(request: HttpRequest) -> dict:
    """
    Instantiate the cart object and make it available to all templates as a variable named "cart".

    It will be executed every time a template is rendered using Django’s RequestContext.
    https://docs.djangoproject.com/en/4.1/ref/templates/api/#django.template.RequestContext

    NB: Context processors are executed in all the requests that use RequestContext. You might want to
    create a custom template tag instead of a context processor if your functionality is not needed in
    all templates, especially if it involves database queries.
    """
    return {
        "cart": Cart(request),
    }
