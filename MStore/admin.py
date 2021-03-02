from django.contrib import admin
from .models.productModel import ProductModel, Brand
from .models.categoryModel import Category
from .models.customerModel import Customer
from .models.cartModel import Cart, CartItem
from .models.productImageModel import ProductImage, Variation
from .models.coupon import Coupon
from .models.tags import tags
# Register your models here.

class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'sales_price', 'slug', 'description', 'uploaded', 'rating', 'active']

class AdminCategory(admin.ModelAdmin):
    list_display = ['id', 'name']

class AdminCustomer(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'phone_number', 'email', 'password']

class CouponAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'number', 'percentage', 'active']


class CartAdmin(admin.ModelAdmin):
    class Meta:
        model = Cart


admin.site.register(Category, AdminCategory)
admin.site.register(Customer, AdminCustomer)

admin.site.register(ProductImage)
admin.site.register(ProductModel, AdminProduct)
admin.site.register(Brand)


admin.site.register(CartItem)
admin.site.register(Cart, CartAdmin)
admin.site.register(Variation)
admin.site.register(tags)

admin.site.register(Coupon, CouponAdmin)
