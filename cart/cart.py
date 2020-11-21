from application.models import Product
from .models import CartDb


class Cart(object):
    def __init__(self, user_id):
        self.user_id = user_id
        cart = []
        cart_db = CartDb.objects.filter(user_id=self.user_id)
        for item in cart_db:
            cart.append(item.product_id)
        self.cart = cart

    def add(self, product):
        if product.id not in self.cart:
            cart_db = CartDb()
            cart_db.user_id = self.user_id
            cart_db.product_id = product.id
            cart_db.save()
            self.cart.append(product.id)

    def remove(self, product):
        product_id = product.id
        if product_id in self.cart:
            CartDb.objects.filter(user_id=self.user_id, product_id=product.id).delete()
            self.cart.remove(product_id)

    def __iter__(self):
        products = Product.objects.filter(id__in=self.cart)
        for product in products:
            yield product

    def __len__(self):
        return len(self.cart)
