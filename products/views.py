from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Offer

# /products --> index
# Uniform Resource Locator (URL) --> Uniform Resource Identifier (URI)


def index(request):
    products = Product.objects.all()  # fetch all products from the database
    offers = Offer.objects.all()  # fetch all offers from the database
    # return HttpResponse("Hello, this is the products index page.")
    return render(request, 'index.html', 
                  {'products': products, 'offers': offers})




def new(request):
    return HttpResponse("New products")