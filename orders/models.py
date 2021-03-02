from django.db import models
from MStore.models.cartModel import Cart, CartItem
from MStore.models.customerModel import Customer

# Create your models here.


STATUS_CHOICES = (
    ("Received", "Received"),
    ("Abandoned", "Abandoned"),
    ("OnDelivery", "OnDelivery"),
    ("Delivered", "Delivered"),
)


class Order(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    order_id = models.CharField(max_length=120, default='abcde', unique=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    status = models.CharField(max_length=120, choices=STATUS_CHOICES, default="Received")

    sub_total = models.DecimalField(max_length=100, max_digits=1000, decimal_places=2, default=0.00)
    tax_total = models.DecimalField(max_length=100, max_digits=1000, decimal_places=2, default=0.00)
    final_total = models.DecimalField(max_length=100, max_digits=1000, decimal_places=2, default=0.00)
    shipping = models.ForeignKey("UserAddress", on_delete=models.SET_NULL, null=True, blank=True, related_name="user_address_shipping_default")
    billing = models.ForeignKey("UserAddress", on_delete=models.SET_NULL, null=True, blank=True, related_name="user_address_billing_default")

    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.order_id

    def get_final_amount(self):
        instance = Order.objects.get(id = self.id)
        instance.tax_total = 0.08 * float(self.sub_total)
        instance.final_total = float(self.sub_total) + instance.tax_total
        instance.save()
        return self.final_total


class UserDefaultAddress(models.Model):
    user = models.OneToOneField(Customer, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return str(self.user.first_name)


class UserAddressManager(models.Manager):
    def get_billing_addresses(self, user):
        return super(UserAddressManager, self).filter(billing=True).filter(user=user)


    # User Address
class UserAddress(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    address = models.CharField(max_length=400)
    address2 = models.CharField(max_length=400, null=True, blank=True)
    city = models.CharField(max_length=120)
    state = models.CharField(max_length=120, null=True, blank=True)
    country = models.CharField(max_length=150)
    postalcode = models.CharField(max_length=30)
    phone = models.CharField(max_length=120)
    shipping = models.BooleanField(default=True)
    billing = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    default = models.BooleanField(default=False)

    objects = UserAddressManager()

    def __str__(self):
        return str(self.address)

    def get_address(self):
        return "%s, %s, %s, %s, %s " %(self.address, self.city, self.state, self.country, self.postalcode)

