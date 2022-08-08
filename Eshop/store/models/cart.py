from django.db import models
# from django.contrib.auth.models import User
from .customer import Customer
from datetime import datetime

from .products import Product

class Cart(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=datetime.now)

    # def __str__(self):
    #     return self.user

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    # price_ht = models.FloatField(blank=True)
    # price=models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)

    # def __str__(self):
    #     return self.product

#     TAX_AMOUNT = 19.25

    # def price_ttc(self):
    #     return self.price_ht * (1 + TAX_AMOUNT/100.0)

    # def __str__(self):
    #     return  self.client + " - " + self.product