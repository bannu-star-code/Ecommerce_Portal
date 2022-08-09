from traceback import print_tb
from django.shortcuts import render , redirect , HttpResponseRedirect
from django.views import  View

from store.models.customer import Customer
from ..models.products import Product
from ..models.order import Order
from ..models.cart import Cart, CartItem


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
        customer=request.session["customer"]
        c=Cart.objects.filter(user=customer)
        for i in c:
            cartitem=CartItem.objects.filter(cart=i)
        dicc={}
        try:
          for i in cartitem:
            dicc[i.product.id]=i.quantity
            # l.append(i.product.id)
            # m.append(i.quantitiy)
            # pass
        except:
            pass
        cart_keys=list(dicc.keys())
        allprods=Product.objects.filter(id__in=cart_keys)
        # print(Product.objects.filter(id__in=cart_keys))
        # print("get",Product.objects.get(id=1))
        # print("c",c)
        
       
        order=Order.objects.create(customer=Customer(id=customer),price=int(price),quantity=sum(dicc.values())
        )
        order.product.set(allprods)
        print("order",Order.product)
        print("lennnn",len(order.product.all()))
        print("asss",order.product.all())
        order.save()
        request.session["cart"]={}
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


    