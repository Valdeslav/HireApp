from django.shortcuts import render
from django.http import HttpResponseRedirect

from .models import Product

from .forms import UpdateProdForm, CreateProdForm


def index(request):
    products = Product.objects.all()
    return render(request, "index.html", {"products": products})


def edit_product(request):
    id = request.GET.get("id", None)
    if id:
        product = Product.objects.get(id=id)
        def_val = {'id': product.id, 'name': product.name, 'cost': product.cost}
        product_form = UpdateProdForm(initial=def_val)
    else:
        product_form = CreateProdForm()
    return render(request, 'edit-product.html', {"form": product_form})


def save_product(request):
    if request.method == "POST":
        id = request.POST.get("id")
        product = Product()

        if id:
            name = request.POST.get("name")
            cost = request.POST.get("cost")
            Product.objects.filter(id=id).update(name=name, cost=cost)

        else:
            product.name = request.POST.get("name")
            product.cost = request.POST.get("cost")
            product.save()

    return HttpResponseRedirect("/")





