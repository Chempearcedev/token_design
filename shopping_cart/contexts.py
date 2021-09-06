from decimal import Decimal
from django.conf import settings
from products.models import Product
from django.shortcuts import get_object_or_404


def cart_contents(request):

    cart_items = []
    total = 0
    product_count = 0
    shopping_cart = request.session.get('shopping_cart', {})

    for item_id, quantity in shopping_cart.items():
        product = get_object_or_404(Product, pk=item_id)
        total += quantity * product.price
        product_count += quantity
        cart_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
        })

    if total < settings.FREE_DELIVERY_POINT:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_POINT - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    context = {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_point': settings.FREE_DELIVERY_POINT,
        'grand_total': grand_total,
    }

    return context
