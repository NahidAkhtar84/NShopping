from django import template
from MStore.models.productModel import Brand
register = template.Library()


@register.filter(name ='brand_product_count')
def brand_product_count(brandname):
    try:
        return Brand.brand_count(brandname)
    except:
        return None

@register.filter(name ='quantity_price_multiplication')
def quantity_price_multiplication(price, quantity):
    return price * quantity


@register.filter(name ='currency_sign')
def currency_sign(currency):
    return '৳ '+str(currency)