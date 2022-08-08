from django import forms
from .models.cart import CartItem
class CartItemForm(forms.ModelForm):
    class Meta:
        model=CartItem
        fields=['product','quantity','cart']
        # labels=['product','quantity','cart']