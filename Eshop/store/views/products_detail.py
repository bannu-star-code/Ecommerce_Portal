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
from django.views.generic import (DetailView)

class ProductDetailView(DetailView):
    model=Product