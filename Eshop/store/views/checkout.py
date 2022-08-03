from traceback import print_tb
from django.shortcuts import render , redirect , HttpResponseRedirect
from django.views import  View

from store.models.customer import Customer
from ..models.products import Product
from ..models.order import Order

class Checkout(View):
    def get(self,request):
        customer=request.session.get('customer')
        print(customer)
        return redirect("orders")
    def post(self,request):
        address=request.POST["address"]
        phone=request.POST["Phone"]
        price=request.POST["Total_price"]
        cart=request.session["cart"]
        cart_keys=list(cart.keys())
        allprods=Product.objects.filter(id__in=cart_keys)
        # print(Product.objects.filter(id__in=cart_keys))
        # print("get",Product.objects.get(id=1))
        customer=request.session["customer"]
        # print(price)
        # print(customer)
        print(allprods)
        # order=Order(
        # customer=Customer(id=customer),
        # price=int(price),
        # address=address,
        # phone=phone,
        # )
        # # for prod in allprods:
        # order.product.set(allprods)
        # order.save()
        # cart={}
        
        print(sum(list(cart.values())))
        order=Order.objects.create(customer=Customer(id=customer),price=int(price),quantity=sum(list(cart.values()))
        )
        order.product.set(allprods)
        print("order",Order.product)
        print("lennnn",len(order.product.all()))
        print("asss",order.product.all()[1].quantity)
        order.save()
        # request.session["cart"]={}
        return redirect('cart')

        # return redirect("orders")
    # def post(self,request):
    #     # print(request.POST)
    #     address=request.POST.get('address')
    #     phone=request.POST.get('phone')
    #     customer=request.session.get('customer')
    #     print(customer)
    #     cart=request.session.get('cart')
    #     products=Product.get_products_by_id(list(cart.keys()))

    #     for product in products:
    #         # print(cart[str(product.id)])
    #         # print(product.id)
    #         order= Order(customer=Customer(id=customer),
    #                      product=product,
    #                      price=product.price*cart[str(product.id)],
    #                      address=address,
    #                      phone=str(phone),
    #                      quantity=cart.get(str(product.id)),)

    #         order.save()
    #     request.session['cart']={}

    #     # return redirect('cart')
    #     return redirect('orders')


    