from email.policy import HTTP
from http.client import HTTPResponse
from tkinter import E
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponse
from matplotlib import category
from store.models.products import Product
from ..models.category import Category
from ..models.customer import Customer
from django.views import View
from ..models.cart import Cart
from ..models.cart import CartItem
from django.views import View
from ..forms import CartItemForm



# print(make_password('123456'))
# print(check_password('123456','pbkdf2_sha256$260000$LWC2qOHXfBANGGPWpyoB8q$pMFvnnoX4J108bXlu/quFRDmIkkSKNYWfEX364Qe/mc='))
# Create your views here.
class Index(View):
    def post(self,request):
        product=request.POST.get('product')
        remove=request.POST.get('remove')
        cart=request.session.get('cart')
        if product:
            if cart:
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
            favourite.pop(fav)

        customer=request.session.get('customer')
        c=Cart.objects.filter(user=customer)
        for i in c:
            cartitem=CartItem.objects.filter(cart=i)
        print(request.POST)
        if request.POST:
            v=True
            try:
              pp=request.POST["product"]
              print("pp",pp)
              if pp:
                for i in cartitem:
                  if int(pp)==int(i.product.id):
                    q=CartItem.objects.get(pk=i.id)
                    a=q.quantity
                    a+=1
                    q.quantity=a
                    q.save(update_fields=['quantity'])             
                    v=False
            except:
                pass
              
            try:
                rr=request.POST["rem"]
                for i in cartitem:
                  if int(rr)==int(i.product.id):
                    q=CartItem.objects.get(pk=i.id)
                    a=q.quantity
                    a-=1
                    q.quantity=a
                    q.save(update_fields=['quantity'])             
                    v=False
             
            except:
                pass 
            if v:
                s=CartItemForm(request.POST)
                if s.is_valid():
                    s.save()
    
        
        return redirect('homepage')

    def get(self,request):
        cart=request.session.get('cart')
        if not cart:
            request.session['cart']={}
        categoryid = request.GET.get('category')
        nothing=""
        if 'query' in request.GET or categoryid:
            if categoryid:
                products= Product.get_all_products_by_id(categoryid)
            else:
               query=request.GET.get('query')
               products=Product.objects.filter(name__icontains=query)
               if len(products)==0:
                  nothing="Nothing Found"
        else:
            products=Product.objects.all()

        d = {}
        # Database CART CODE
        customer=request.session.get('customer')
        c=Cart.objects.filter(user=customer)
        # print("c",c)
        if customer:
            s= CartItemForm()
            d['customer']=customer
        else:
            s="Not logged in"
        for i in c:
            
            cartitem=CartItem.objects.filter(cart=i)
            s= CartItemForm(initial={'cart': i})
            d["i"]=i.id
           
            if cartitem:
              d["cartitem"]=cartitem
        dicc={}
        try:
          for i in cartitem:
            dicc[i.product.id]=i.quantity
            # l.append(i.product.id)
            # m.append(i.quantitiy)
            # pass
        except:
            pass
        # print(sum(dicc.values()))
        # print(dicc[2])
        d["total_quantity"]=sum(dicc.values())
        d["products"]=products
        d["form"]=s
        d["pro_list"]=dicc     
        d['products']=products
        d['categories']=Category.get_all_categories()
        d["nothing"]=nothing


        return render(request, 'index.html', d)

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
