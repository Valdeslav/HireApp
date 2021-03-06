from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect

from application.models import Product, Category

from application.forms import UpdateProdForm, CreateProdForm


def index(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    # if button "удалить" pressed
    is_delete = request.GET.get("delete")
    if is_delete:
        return render(request, "product/index.html", {"products": products, "is_delete": True})

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    return render(request, "catalog/catalog.html", {"products": products, 'category': category, 'categories': categories})


def edit_product(request):
    id = request.GET.get("id", None)
    if id:
        product = Product.objects.get(id=id)
        def_val = {'id': product.id, 'name': product.name, 'cost': product.cost}
        product_form = UpdateProdForm(initial=def_val)
    else:
        product_form = CreateProdForm()
    return render(request, 'product/edit-product.html', {"form": product_form})


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


def delete_product(request):
    if request.method == "POST":
        ids = request.POST.getlist("id")
        for id in ids:
            Product.objects.filter(id=id).delete()

    return HttpResponseRedirect("/")





