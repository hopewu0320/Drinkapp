from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Drink,Cart
# Create your views here.

def home(request):
    drinks = Drink.objects.all()
    context = {'drinks':drinks}
    return render(request, 'base/home.html',context)

def productinfo(request,pk):
    drink = Drink.objects.get(id=pk)
    context = {'drink':drink}
    return render(request, 'base/productinfo.html',context)

#需要物品的數量 價錢
def addtocart(request,pk):    #東西加入完購物車 導向cart
    drink = Drink.objects.get(id=pk)
    total = drink.price
    if request.method == "POST":
        Cart.objects.create(
        drink = drink,
        total = total
        )
        context = {'total':total}
        return redirect('cart')
    #context = {'total':total}
    #return render(request, 'base/addtocart.html',context)
def cart(request):
    carts =Cart.objects.all()
    total = 0
    for cart in carts:
        total+=cart.drink.price
    context = {'carts':carts,'total':total}
    return render(request, 'base/cart.html',context)