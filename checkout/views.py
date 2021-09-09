from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    shopping_cart = request.session.get('shopping_cart', {})
    if not shopping_cart:
        messages.error(request, "There's nothing in your shopping cart at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51JXmvfCQPN1jVqIk0BNSyK6P7HdqyyqK8mmcITtAOg5392SjNBBTx6vUUmehDN7L0OY4fu7q2ViFSiRybiRyjwIG009tmEpyTh'
    }

    return render(request, template, context)
