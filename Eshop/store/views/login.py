from django.shortcuts import render , redirect , HttpResponseRedirect

from django.contrib.auth.hashers import  check_password
from store.models.customer import Customer
from django.views import  View

class Login(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        email=request.POST.get('email')
        password=request.POST.get('password')
        customer=Customer.get_customer_by_email(email) 
        print(customer)
        error_messages=None
        if customer:
            flag=check_password(password, customer.password)
            if flag:
                request.session['customer']=customer.id
                # print(request.session.customer)
                request.session['email']=customer.email
                print(customer)
                print(customer.id)
                return redirect('homepage')
            else:
                error_messages='Email or Password Invalid'
        else:
            error_messages='Email or Password Invalid'
        print(email, password)
        return render(request, 'login.html', {'error':error_messages})

def logout(request):
    request.session.clear()
    return redirect('login')