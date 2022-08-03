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


# print(make_password('123456'))
# print(check_password('123456','pbkdf2_sha256$260000$LWC2qOHXfBANGGPWpyoB8q$pMFvnnoX4J108bXlu/quFRDmIkkSKNYWfEX364Qe/mc='))
# Create your views here.
class Index(View):
    def post(self,request):
        product=request.POST.get('product')
        # print("product",product)
        remove=request.POST.get('remove')
        cart=request.session.get('cart')
        if product:
            if cart:
            #   print(cart)
              quantity=cart.get(product)
              if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product]=quantity-1
                else:
                    cart[product]=quantity+1
              else:
                cart[product]=1
            
            else:
               cart={}
               cart[product]=1
            request.session['cart']=cart
        fav=request.POST.get('fav')
        remove1=request.POST.get('remove1')
        favourite=request.session.get('favourite')
        if fav:
            if favourite:
                 favourite[fav]=1
            else:
                 favourite={}
                 favourite[fav]=1
            request.session['favourite']=favourite
             
        if remove1:
            # print('remove',remove1)
            favourite.pop(fav)
            # print("after remove",request.session.get('favourite'))
        return redirect('homepage')

    def get(self,request):
        cart=request.session.get('cart')
        if not cart:
            request.session['cart']={}
        categoryid = request.GET.get('category')
        nothing=""
        # print("caaaa",categoryid)
        if 'query' in request.GET or categoryid:
            if categoryid:
                products= Product.get_all_products_by_id(categoryid)
        #     print(products)
            else:
               query=request.GET.get('query')
            #    print(query)
               products=Product.objects.filter(name__icontains=query)
               if len(products)==0:
                  nothing="Nothing Found"
        else:
            products=Product.objects.all()
        c = {}
        c['products']=products
        c['categories']=Category.get_all_categories()
        c["nothing"]=nothing

        # print(request.session.get('email'))
        # print(request.session.get('customer_id'))
        return render(request, 'index.html', c)

# def index(request):
#     categoryid = request.GET.get('category')
#     if categoryid:
#         products= Product.get_all_products_by_id(categoryid)
#     else:
#         products= Product.get_all_products()
#     c = {}
#     c['prod']=products
#     c['categories']=Category.get_all_categories()
#     print(request.session.get('email'))
#     print(request.session.get('customer_id'))
#     return render(request, 'index.html', c)
