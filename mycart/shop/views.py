from django.shortcuts import render
from django.http import HttpResponse 
from .models import product
from math import ceil, prod

# Create your views here.

def index(request):
    # products = product.objects.all()
    # print ( products )
    # n = len(products)
    # nSlides = n//4 + ceil((n/4)-n//4)

    allprods = []
    catprods = product.objects.values('product_category','id')
    cats = {item['product_category'] for item in catprods}
    for cat in cats:
        prod = product.objects.filter(product_category=cat)
        n = len(prod)
        nslides = n//4 + ceil((n/4)-n//4)
        allprods.append([prod,range(1,nslides),nslides])
    # allprods = [[products, range(1,nSlides),nSlides],
    #             [products, range(1,nSlides),nSlides]]

    params = {'allprods':allprods}
    # params = {'no_of_slides': nSlides, 'range':range(1,nSlides), 'product': products}
    return render(request,'shop/index.html', params)

def about(request):
    return render(request,'shop/about.html')

def contact(request):
    return render(request,'shop/contact.html')

def tracker(request):
    return render(request,'shop/tracker.html')

def search(request):
    return render(request,'shop/search.html')

def ProductView(request,myid):
    # fetch the product using ID 
    products = product.objects.filter(id=myid)
    print(products)
    prodict = {'product':products[0]}
    return render(request,'shop/prodview.html',prodict)

def checkout(request):
    return render(request,'shop/checkout.html')

