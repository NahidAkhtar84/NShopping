from django.shortcuts import render, redirect, HttpResponseRedirect
from django.views import View
from MStore.models.cartModel import Cart, CartItem
from MStore.models.productModel import ProductModel
from MStore.models.productImageModel import Variation
from django.urls import reverse
from MStore.models.coupon import Coupon
from .coupon import couponapply


# login class
class Basket(View):

    def get(self, request):
        try:
            the_id = request.session["cart_id"]
            cart = Cart.objects.get(id=the_id)
        except:
            the_id = None
        if the_id:
            new_total = 0.00
            for p in cart.cartitem_set.all():
                line_total = float(p.product.price) * p.quantity
                new_total += line_total
            request.session["item_counts"] = cart.cartitem_set.count()
            cart.total = round(new_total, 2)
            cart_total = cart.total

            try:
                coupon = request.session.get('coupon')
                cpn = Coupon.objects.filter(name=coupon)[0]

                if not cpn.percentage:
                    cart_total = cart_total - float(cpn.number)
                else:
                    cart_total = cart_total - (cart_total * float(cpn.number) / 100)
            except:
                pass
            cart.coupontotal = cart_total

            cart.save()
            context = {'cart': cart}
        else:
            empty_msg = "Your Cart is empty. Please keep shopping!"
            context = {"empty": True, "empty_msg": empty_msg}

        return render(request, 'basket.html', context)

    def post(self, request):
        try:
            the_id = request.session["cart_id"]
            cart = Cart.objects.get(id=the_id)
        except:
            the_id = None
        if the_id and cart.couponapplied == False:
            cart_total = Cart.objects.get(id=the_id).total
            coupon = request.POST.get('coupon')
            request.session['coupon'] = coupon
            try:
                cpn = Coupon.objects.filter(name=coupon)[0]
                # field_value = getattr(cpn, 'number')
            except:
                pass

            if not cpn.percentage:
                cart_total = cart_total - cpn.number
            else:
                cart_total = cart_total - (cart_total * cpn.number / 100)
            cart.coupontotal = cart_total
            cart.couponapplied = True
            cart.save()
            return redirect('basket')
        # else:
        #     context = {"errormsg": }

def remove_from_cart(request, id):
    try:
        the_id = request.session["cart_id"]
        cart = Cart.objects.get(id=the_id)
    except:
        return HttpResponseRedirect(reverse("basket"))
    cartitem = CartItem.objects.get(id=id)
    # This way can also be done
    # cartitem.delete()
    cartitem.cart = None
    cartitem.save()
    return HttpResponseRedirect(reverse("basket"))


def add_to_cart(request, slug):

    try:
        the_id = request.session["cart_id"]
    except:
        new_cart = Cart()
        new_cart.save()
        the_id = new_cart.id
        request.session["cart_id"] = new_cart.id

    cart = Cart.objects.get(id=the_id)
    try:
        product = ProductModel.objects.get(slug=slug)
    except ProductModel.DoesNotExist:
        pass
    except:
        pass
    product_var = []
    if request.method == 'POST':
        qty = request.POST['qty']
        proname = request.POST['proname']
        for item in request.POST:
            key = item
            val = request.POST[key]
            print('key', key)
            print('val', val)
            try:
                v = Variation.objects.get(product=proname, category__iexact=key, name__iexact=val)
                product_var.append(v)
                print('product var:',product_var)
            except Exception as e:
                print("Exception:", e)
                pass

        cart_item = CartItem.objects.create(cart=cart, product=product)

        if len(product_var) > 0:
            cart_item.variations.add(*product_var)
        cart_item.quantity = qty
        cart_item.save()
        return HttpResponseRedirect(reverse("basket"))
    else:
        return HttpResponseRedirect(reverse("basket"))