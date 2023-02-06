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

#按下購物車按鈕 商品的amount數量上升
#如果drink.name not exist,create object else 加入
#https://stackoverflow.com/questions/11714536/check-if-an-object-exists
#用filter 可以數物品數
def addtocart(request,pk):    #東西加入完購物車 導向cart
    drink = Drink.objects.get(id=pk)
    if request.method == "POST":
        if Cart.objects.filter(drink=drink).exists():
            cart = Cart.objects.get(drink=drink)
            cart.amount = cart.amount+1
            cart.save()
        else:
            Cart.objects.create(
            drink = drink,
            name = drink.name,
            amount=1,
            )  
        return redirect('cart')
    #context = {'total':total}
    #return render(request, 'base/addtocart.html',context)
def cart(request):
    carts = Cart.objects.all()
    total = 0 
    for cart in carts:
        total+=cart.drink.price
    context = {'carts':carts,'total':total}
    return render(request, 'base/cart.html',context)

