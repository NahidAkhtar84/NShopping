from django.db import models
from .productModel import ProductModel


class ProductImage(models.Model):
    product = models.ForeignKey(ProductModel, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(upload_to='Uploads/products/')
    featured = models.BooleanField(default=False)
    thumbnail = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.product.name


class VariationManager(models.Manager):
    def all(self):
        return super(VariationManager, self).filter(active=True)

    def sizes(self):
        return self.all().filter(category='size')

    def colors(self):
        return self.all().filter(category='color')


VAR_CATEGORIES = {
    ('size', 'size'),
    ('color', 'color'),
    ('package', 'package'),
}


class Variation(models.Model):
    product = models.ForeignKey(ProductModel, on_delete=models.SET_NULL, null=True, blank=True)
    category = models.CharField(max_length=120, choices=VAR_CATEGORIES, default='size')
    name = models.CharField(max_length=120)
    image = models.ForeignKey(ProductImage, on_delete=models.SET_NULL, null=True, blank=True)
    price = models.DecimalField(max_digits=100, decimal_places=10, null=True, blank=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    active = models.BooleanField(default=True)

    objects = VariationManager()

    def __str__(self):
        return self.name
