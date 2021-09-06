from django.shortcuts import render, redirect


def view_cart(request):

    return render(request, 'shopping_cart/shopping_cart.html')


def add_to_cart(request, item_id):

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    shopping_cart = request.session.get('shopping_cart', {})

    if item_id in list(shopping_cart.keys()):
        shopping_cart[item_id] += quantity
    else:
        shopping_cart[item_id] = quantity

    request.session['shopping_cart'] = shopping_cart
    print(request.session['shopping_cart'])
    return redirect(redirect_url)
