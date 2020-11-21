from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.http import urlencode
from django.views.decorators.http import require_POST
from application.models import Product
from .cart import Cart


@require_POST
def cart_add(request, product_id):
    if not request.user.is_authenticated:
        url_param = urlencode({'scmsg': 'Войдите чтобы добавлять товары в корзину'})
        http_response = HttpResponseRedirect(f'/login?{url_param}')
        return http_response

    cart = Cart(request.user.id)
    product = get_object_or_404(Product, id=product_id)
    cart.add(product)
    return redirect('/')


def cart_remove(request, product_id):
    cart = Cart(request.user.id)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('/cart-detail/')


def cart_detail(request):
    if not request.user.is_authenticated:
        url_param = urlencode({'scmsg': 'Войдите чтобы просмотреть свои заказы'})
        http_response = HttpResponseRedirect(f'/login?{url_param}')
        return http_response

    cart = Cart(request.user.id)
    return render(request, 'cart/detail.html', {'cart': cart})
