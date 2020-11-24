from _datetime import datetime

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils.http import urlencode
from django.views.decorators.http import require_GET, require_POST


from cart.models import CartDb
from application.models import Product
from .models import Hire, HireElement


@require_GET
def make_order(request):
    if not request.user.is_authenticated:
        url_param = urlencode({'scmsg': 'Войдите чтобы совершать заказы'})
        http_response = HttpResponseRedirect(f'/login?{url_param}')
        return http_response

    cart = CartDb.objects.filter(user_id=request.user.id)
    product_ids = []
    for item in cart:
        product_ids.append(item.product_id)
    products = Product.objects.filter(id__in=product_ids)
    today = datetime.today()
    today = today.strftime('%Y-%m-%d')
    message = request.GET.get("message")
    return render(request, 'orders/make_order.html', {'products': products, 'today': today, 'message': message})


@require_POST
def complite_order(request):
    taking_date = request.POST.get("taking_date")
    return_date = request.POST.get("return_date")
    taking_date = datetime.strptime(taking_date, '%Y-%m-%d')
    return_date = datetime.strptime(return_date, '%Y-%m-%d')
    cost = request.POST.get('inputCost')
    hire = Hire(hirer=request.user.id, taking_date=taking_date, return_date=return_date, cost=cost)
    if 'order_paid' in request.POST:
        hire.paid = True
    elif 'order_save' in request.POST:
        hire.paid = False
    hire.save()

    # saving Hire elements
    product_ids = request.POST.getlist("checked_product")
    for id in product_ids:
        




