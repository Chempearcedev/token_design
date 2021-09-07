from django.shortcuts import render, redirect, reverse, HttpResponse


def view_cart(request):

    return render(request, 'shopping_cart/shopping_cart.html')


def add_to_cart(request, item_id):

    quantity = int(request.POST.get('quantity'))
    shopping_cart = request.session.get('shopping_cart', {})

    if item_id in list(shopping_cart.keys()):
        shopping_cart[item_id] += quantity
    else:
        shopping_cart[item_id] = quantity

    request.session['shopping_cart'] = shopping_cart
    return redirect(reverse('view_cart'))


def update_cart(request, item_id):

    quantity = int(request.POST.get('quantity'))
    shopping_cart = request.session.get('shopping_cart', {})

    if quantity > 0:
        shopping_cart[item_id] = quantity
    else:
        del shopping_cart[item_id]
        
        if quantity > 0:
            shopping_cart[item_id] = quantity
        else:
            shopping_cart.pop(item_id)

    request.session['shopping_cart'] = shopping_cart
    return redirect(reverse('view_cart'))
