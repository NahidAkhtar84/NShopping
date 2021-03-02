from django.contrib import admin
from .models import Order, UserAddress, UserDefaultAddress

# Register your models here.
class UserAddressAdmin(admin.ModelAdmin):
    list_display = ['id', 'address']

admin.site.register(Order)
admin.site.register(UserAddress, UserAddressAdmin)
admin.site.register(UserDefaultAddress)