from django.shortcuts import render , redirect , HttpResponseRedirect
from django.views import  View

from store.models.customer import Customer
from ..models.products import Product
from ..models.order import Order
from store.middlewares.auth import auth_middleware
from django.utils.decorators import method_decorator

class Orders(View):
    # @method_decorator(auth_middleware)
    def get(self, request):
        # del_order=request.GET["del_order"]
        # if del_order:
        #     print(del_order)
        customer=request.session.get('customer')
        # print(customer)
        orders=Order.get_orders_by_customer_id(customer)
        # for i in orders:
        #     print(i.product.all())
        # print(orders.product)
        # print(orders)
        return render(request, 'orders.html', {'orders':orders})