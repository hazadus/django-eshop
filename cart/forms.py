from django import forms

PRODUCT_QTY_CHOICES = [(i, str(i)) for i in range(1, 21)]


class CartAddProductForm(forms.Form):
    """
    Form to add products to the cart.

    quantity: allows user to select a quantity between 1 and 20, with coerce=int to convert the input into an integer.
    override: allows us to indicate whether we want to add (False) or override existing value (True).
              Here we use HiddenInput since we don't want to display it to the user.
    """
    quantity = forms.TypedChoiceField(choices=PRODUCT_QTY_CHOICES, coerce=int)
    override = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
