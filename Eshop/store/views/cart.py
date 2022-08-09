from email.policy import HTTP
from http.client import HTTPResponse
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponse
from matplotlib import category
from store.models.products import Product
from ..models.category import Category
from ..models.customer import Customer
from ..models.cart import Cart
from ..models.cart import CartItem
from django.views import View
from ..forms import CartItemForm

# class NewCart(View):
#     def get(self,request):


class CartView(View):
    # class Cart(View):
    def post(self, request):
        # print(request.POST)
        cart=request.session["cart"]
        ids=list(cart)
        print("requestpost",request.POST)
        s=CartItemForm(request.POST)
        if s.is_valid():
            print("cartrequestpost",request.POST)
            s.save()
        products=Product.get_products_by_id(ids)
        return redirect("cart")
        # return render(request, 'cart.html',{'products':products})
    def get(self, request):
        # print(request.GET["del"])
        dell=request.GET.get("del")
        add=request.GET.get("add")
        cart=request.session["cart"]
        if add:
            cart[add]+=1
        if dell:
            if cart[dell]>1:
               cart[dell]-=1
            else:
               cart.pop(dell)

        request.session['cart']=cart
        ids=list(request.session['cart'].keys())
        products=Product.get_products_by_id(ids)
        customer=request.session.get('customer')
        print(customer)

        # Database CART CODE

        
        print("customer",Customer.objects.filter(id=customer))
        # cartitem=CartItem.objects.all()
        c=Cart.objects.filter(user=customer)
        # carti=CartItem.objects.filter(cart=1)
        print("c",c)
        d={}
        if customer:
            s= CartItemForm()
            d['customer']=customer
        else:
            s="Not logged in"
        for i in c:
            print("i",i)
            cartitem=CartItem.objects.filter(cart=i)
            s= CartItemForm(initial={'cart': i})
            if cartitem:
              d["cartitem"]=cartitem
            print(cartitem)
        d["products"]=products
        d["form"]=s



        return render(request, 'cart.html',d)