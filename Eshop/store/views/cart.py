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
from django.views import View


class Cart(View):
    def post(self, request):
        print(request.POST)
        cart=request.session["cart"]
        ids=list(cart)
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
        return render(request, 'cart.html',{'products':products})