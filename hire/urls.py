"""hire URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, re_path

from application import views
from accounts import views as account_views
from cart import views as cart_views
from orders import views as orders_views

urlpatterns = [
    path('', views.index, name='product_list'),
    path('edit-product', views.edit_product),
    path('save-product', views.save_product),
    path('delete-product', views.delete_product),

    path('login/', account_views.user_login, name='login'),
    path('logout/', account_views.user_logout, name='logout'),
    path('register/', account_views.register, name='register'),
    path('admin/', admin.site.urls),

    path('cart-detail/', cart_views.cart_detail, name='cart_detail'),

    path('make-order/', orders_views.make_order, name='make_order'),
    path('complite-order/', orders_views.complite_order, name='complite_order'),
    path('order-list/', orders_views.order_list, name="order_list"),
    re_path(r'^order/(?P<order_id>\d+)/$', orders_views.order_details, name='order_details'),
    re_path(r'^remove-saved-order/(?P<order_id>\d+)/$', orders_views.remove_saved_order, name='remove-saved-order'),

    re_path(r'^add/(?P<product_id>\d+)/$', cart_views.cart_add, name='cart_add'),
    re_path(r'^remove/(?P<product_id>\d+)/$', cart_views.cart_remove, name='cart_remove'),

    re_path(r'^(?P<category_slug>[-\w]+)/$', views.index, name='product_list_by_category'),
]
