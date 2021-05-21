from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.

def index(request):
    return render(request,'shop/index.html')

def about(request):
    return render(request,'shop/about.html')

def contact(request):
    return HttpResponse("we are at the contact page.")

def tracker(request):
    return HttpResponse("we are at the Product tracker page.")

def search(request):
    return HttpResponse("we are at the search page.")

def ProductView(request):
    return HttpResponse("we are at the Product View page.")

def checkout(request):
    return HttpResponse("we are at the checkout page.")

