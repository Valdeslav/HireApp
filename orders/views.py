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
    hire = Hire(hirer=request.user.id, taking_date=taking_date, return_date=return_date, cost=cost, number=0)
    if 'order_paid' in request.POST:
        hire.paid = True
    elif 'order_save' in request.POST:
        hire.paid = False
    hire.save()

    # saving Hire elements
    product_ids = request.POST.getlist("checked_product")
    cart = CartDb.objects.filter(user_id=request.user.id)
    hire_prod_number = 0
    for id in product_ids:
        product = Product.objects.get(id=id)
        number = request.POST.get("number"+str(id))
        hire_element = HireElement(number=number, hire=hire, product=product)
        hire_element.save()
        # delete product from cart
        cart.filter(product_id=id).delete()
        hire_prod_number += int(number)

    hire.number = hire_prod_number
    hire.save()
    return HttpResponseRedirect('/order-list')
        

def order_list(request):
    if not request.user.is_authenticated:
        url_param = urlencode({'scmsg': 'Войдите чтобы посмотреть свои заказы'})
        http_response = HttpResponseRedirect(f'/login?{url_param}')
        return http_response

    paid_orders = Hire.objects.filter(hirer=request.user.id, paid=True)
    saved_orders = Hire.objects.filter(hirer=request.user.id, paid=False)

    return render(request, "orders/order-list.html", {'paid_orders': paid_orders, 'saved_orders': saved_orders})
