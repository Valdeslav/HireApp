from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils.http import urlencode

from  cart.models import CartDb
from application.models import Product


def make_order(request):
    if not request.user.is_authenticated:
        url_param = urlencode({'scmsg': 'Войдите чтобы добавлять товары в корзину'})
        http_response = HttpResponseRedirect(f'/login?{url_param}')
        return http_response

    #if request.method == "GET":
    cart = CartDb.objects.filter(user_id=request.user.id)
    product_ids = []
    for item in cart:
        product_ids.append(item.product_id)
    products = Product.objects.filter(id__in=product_ids)
    return render(request, 'orders/make_order.html', {'products': products})

