from MStore.models.cartModel import Cart
from django.shortcuts import render, redirect
from MStore.models.coupon import Coupon

def couponapply(request):
    try:
        the_id = request.session["cart_id"]
        cart = Cart.objects.get(id=the_id)
    except:
        the_id = None
    if the_id:
        cart_total = Cart.objects.get(id=the_id).total
        coupon = request.POST.get('coupon')
        try:
            cpn = Coupon.objects.filter(name = coupon)[0]
            # field_value = getattr(cpn, 'number')
        except:
            pass
        if not cpn.percentage:
            cart_total = cart_total - cpn.number
        else:
            cart_total = cart_total - (cart_total*cpn.number/100)
        cart.coupontotal = cart_total
        cart.save()
        print('*************************',cart_total)
        return redirect('basket')