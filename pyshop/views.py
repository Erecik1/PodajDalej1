from django.http import HttpResponse
from django.shortcuts import render, redirect
from products.models import Product
from django.contrib.auth.decorators import login_required
from cart.cart import Cart


# Create your views here.
def index(request):
    # return HttpResponse('Hello World')
    products = Product.objects.all()
    return render(request, 'index.html',
                  {'products': products})

def new(request):
        return render(request, 'index.html')    


