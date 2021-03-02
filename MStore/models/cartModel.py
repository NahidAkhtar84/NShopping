from django.db import models
from .productModel import ProductModel
from .productImageModel import Variation


# Create your models here.

class CartItem(models.Model):
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, null=True, blank=True)
    variations = models.ManyToManyField(Variation)
    quantity = models.IntegerField(default=1)
    notes = models.TextField(null=True, blank=True)
    line_total = models.DecimalField(default=1.00, max_digits=1000, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        try:
            return str(self.cart.id)
        except:
            return self.product.name



class Cart(models.Model):
    # items = models.ManyToManyField(CartItem, null=True, blank=True)
    total = models.DecimalField(max_length=100, max_digits=1000, decimal_places=2, default=0.00)
    coupontotal = models.DecimalField(max_length=100, max_digits=1000, decimal_places=2, default=0.00)
    couponapplied = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return "Cart id: %s" % (self.id)
