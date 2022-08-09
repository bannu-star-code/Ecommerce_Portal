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


class Favourite(View):

      def post(self, request):
        print("postFav",request.POST)
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
            print('remove',remove1)
            favourite.pop(fav)
            print("after remove",request.session.get('favourite'))
        return redirect('favourite')

        
      def get(self, request):
        print("fav",request.GET)
        try:
         ids=list(request.session.get('favourite').keys())
        except:
          pass
        #   ids.remove('null')
        # print()
        # print('favortepageids:',ids)
        products=Product.get_products_by_id(ids)
        return render(request, 'favourite.html',{'products':products})

     



    
   