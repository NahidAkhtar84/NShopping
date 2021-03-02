from django.shortcuts import render, HttpResponseRedirect, redirect, Http404
from MStore.models.cartModel import Cart
from django.urls import reverse
from .models import Order, UserAddress, UserDefaultAddress
from .forms import UserAddressForm
import datetime
from .utils import id_generator
from MStore.models.customerModel import Customer
from django.contrib import messages
from MStore.middleware.auth import auth_middleware


# Create your views here.


def orders(request):
    all_orders = Order.objects.all().order_by('-updated')
    context = {"all_orders": all_orders}
    template = "orders/orders.html"
    return render(request, template, context)


def add_user_address(request):
    # print(request.GET)
    # try:
    #     next_page = request.GET.get("next")
    # except:
    #     next_page = None
    if request.method == "POST":
        customer = request.session.get('customer_id')
        pst = request.POST
        address = pst.get('address')
        address2 = pst.get('address2')
        phone = pst.get('phone')
        country = pst.get('country')
        state = pst.get('state')
        city = pst.get('city')
        postalcode = pst.get('postalcode')
        billing = pst.get('billing')
        if pst.get('default') == '1':
            default = True
        else:
            default = False

        if default:
            userdefaultaddress = UserAddress.objects.filter(user = Customer(id=customer))
            userdefaultaddress.update(default=False)

        user_added = UserAddress(
            user=Customer(id=customer),
            address=address,
            address2=address2,
            phone=phone,
            country=country,
            state=state,
            city=city,
            postalcode=postalcode,
            billing=billing,
            default=default
        )
        user_added.save()

        # form = UserAddressForm(request.POST)
        # if form.is_valid():
        #     new_address = form.save(commit=False)
        #     new_address.user = Customer(id=customer)
        #     new_address.save()
        # if next_page is not None:
        #     return HttpResponseRedirect(reverse(str(next_page))+"?address_added=True")
        # else:
        #     raise Http404
        return HttpResponseRedirect(reverse('checkout'))


def checkout(request):
    customer = request.session.get('customer_id')
    try:
        the_id = request.session["cart_id"]
        cart = Cart.objects.get(id=the_id)
    except:
        the_id = None
        return HttpResponseRedirect(reverse("basket"))

    try:
        new_order = Order.objects.get(cart=cart)
    except Order.DoesNotExist:
        new_order = Order(
            user=Customer(id=customer)
        )
        new_order.cart = cart
        new_order.order_id = id_generator()
        new_order.save()
    except Exception as e:
        new_order = None
        return HttpResponseRedirect(reverse("basket"))

    final_amount = 0
    print('order', new_order)
    if new_order is not None:
        if cart.couponapplied:
            new_order.sub_total = cart.coupontotal
        else:
            new_order.sub_total = cart.total

    final_amount = new_order.get_final_amount()
    new_order.save()


    current_address = UserAddress.objects.filter(user=Customer(id=customer))
    billing_address = UserAddress.objects.get_billing_addresses(user=Customer(id=customer))
    buying_user = Customer(id=customer)



    if request.method == "POST":
        # print(UserAddress.objects.get(id = request.POST.get('shipping_address')))
        # print(UserAddress.objects.get(id = request.POST.get('billing_address')))
        new_order.shipping = UserAddress.objects.get(id = request.POST.get('shipping_address'))
        new_order.billing = UserAddress.objects.get(id = request.POST.get('billing_address'))
        new_order.save()
        del request.session["cart_id"]
        del request.session["item_counts"]
        try:
            del request.session["coupon"]
        except:
            pass
        messages.success(request, "Thank You for your purchase. Your order will be delivered on time!")
        return HttpResponseRedirect(reverse("orders"))

    context = {
               "current_address": current_address,
               "billing_address": billing_address,
               "buying_user": buying_user,
               "order": new_order
               }
    template = "orders/checkout.html"
    return render(request, template, context)
