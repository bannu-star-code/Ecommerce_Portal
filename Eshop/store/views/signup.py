from email.policy import HTTP
from http.client import HTTPResponse
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponse
from matplotlib import category
from ..models.products import Product
from ..models.category import Category
from ..models.customer import Customer
from ..models.cart import Cart
from django.views import View




class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')
    def post(self, request):
        postData=request.POST
        first_name=postData.get('firstname')
        last_name=postData.get('lastname')
        phone=postData.get('phone')
        email=postData.get('email')
        password=postData.get('password')
        # validation
        customer=Customer(first_name=first_name,last_name=last_name,phone=phone,
                email=email, password=password)
        value={
            'first_name':first_name,
            'last_name':last_name,
            'phone':phone,
            'email':email
        }
        error_messages=self.validateCustomer(customer)
        # error_messages=None
        print(first_name,last_name)
        if not error_messages:
            customer=Customer(first_name=first_name,last_name=last_name,phone=phone,
                email=email, password=password)
            customer.password=make_password(customer.password)
            customer.register()
            cart=Cart(user=customer)
            # if cart.is_valid():
            cart.save()
            return redirect( 'homepage')
        else:
            data={'error':error_messages,
                #   'values':value
                  }

            return render(request, 'signup.html', data)
        
    def validateCustomer(self,customer):
            error_messages=None
            if (not customer.first_name):
                error_messages='First Name Required !!'
            elif len(customer.first_name)<4:
                error_messages='First Name must be greater than 4'
            elif (not customer.last_name):
                error_messages='last Name Required !!'
            elif len(customer.last_name)<4:
                error_messages='last Name must be greater than 4'
            elif len(customer.phone)<10:
                error_messages='phone number must 10  char long !!'
            elif (not customer.phone):
                error_messages='Phone number required '
            elif len(customer.email)<5:
                error_messages='Email must 5 char long'
            elif customer.isExists():
                error_messages='Email address already exists'

            return error_messages