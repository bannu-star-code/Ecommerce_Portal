from django.contrib import admin
from django.urls import path
from .views.home import Index
from .views.login import Login, logout
from .views.signup import Signup
from .views.cart import CartView
from .views.checkout import Checkout
from .views.orders import Orders
from .views.favourite import Favourite
from .views.products_detail import DetailView, ProductDetailView
from .views import search
urlpatterns = [
    path('', Index.as_view(), name='homepage'),
    path('signup',Signup.as_view(), name='signup'),
    path('login', Login.as_view(), name='login'),
    path('logout', logout, name='logout'),
    path('cart', CartView.as_view(), name='cart'),
    path('check-out', Checkout.as_view(), name='checkout'),
    path('orders', Orders.as_view(), name='orders'),
    path('favourite',Favourite.as_view(), name='favourite'),
    path('product/<int:pk>/', ProductDetailView.as_view()),
    path('search',search.serach)
]