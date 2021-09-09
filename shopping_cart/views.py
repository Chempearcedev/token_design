from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages



from products.models import Product


def view_cart(request):

    return render(request, 'shopping_cart/shopping_cart.html')


def add_to_cart(request, item_id):
    product = Product.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    shopping_cart = request.session.get('shopping_cart', {})

    if item_id in list(shopping_cart.keys()):
        shopping_cart[item_id] += quantity
    else:
        shopping_cart[item_id] = quantity
        messages.success(request, f'You added {product.name} to your shopping cart')

    request.session['shopping_cart'] = shopping_cart
    return redirect(reverse('view_cart'))


def update_cart(request, item_id):
    product = Product.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    shopping_cart = request.session.get('shopping_cart', {})

    if quantity > 0:
        shopping_cart[item_id] = quantity
        messages.success(request, f'Updated {product.name} quantity to {shopping_cart[item_id]}')
        print('Quantity more than 0')
    else:
        shopping_cart.pop(item_id)
        messages.success(request, f'Removed {product.name} from your shopping cart')
        print('Quantity more than 0')

    request.session['shopping_cart'] = shopping_cart
    return redirect(reverse('view_cart'))


def remove_from_cart(request, item_id):
    product = Product.objects.get(pk=item_id)
    shopping_cart = request.session.get('shopping_cart', {})

    shopping_cart.pop(item_id)
    messages.success(request, f'Removed {product.name} from your shopping cart')
    print('Quantity more than 0')

    request.session['shopping_cart'] = shopping_cart
    return HttpResponse(status=200)
