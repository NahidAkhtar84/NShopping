import string
import random
from .models import Order


def id_generator(size=16, chars=string.ascii_uppercase + string.digits):
    ord_id = "".join(random.choice(chars) for x in range(size))
    try:
        order = Order.objects.get(order_id=ord_id)
        id_generator()
    except Order.DoesNotExist:
        return ord_id
