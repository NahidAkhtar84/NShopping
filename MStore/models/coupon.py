from django.db import models

class Coupon(models.Model):
    name = models.CharField(max_length=400)
    number = models.DecimalField(default=0.00, max_digits=1000, decimal_places=2)
    percentage = models.BooleanField(default=False)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.name