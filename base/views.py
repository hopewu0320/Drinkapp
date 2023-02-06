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


#東西加入完購物車 導向cart
def addtocart(request,pk):    
    drink = Drink.objects.get(id=pk)
    if request.method == "POST":
        if Cart.objects.filter(drink=drink).exists():
            cart = Cart.objects.get(drink=drink)
            cart.amount = cart.amount+1
            cart.save()
        else:
            Cart.objects.create(
            drink = drink,
            amount = 1,
            subtotal = 0,
            )  
        return redirect('cart')
    #context = {'total':total}
    #return render(request, 'base/addtocart.html',context)
def cart(request):
    carts = Cart.objects.all()
    total = 0 
    for cart in carts:
        total+=cart.subtotal
    context = {'carts':carts,'total':total}
    return render(request, 'base/cart.html',context)

#更改購物車內容 增加 減少 清空購物車 
#問題:可以把數量減到負數 數量至少為1 小於1就要刪除
def editcart(request,pk):
    drink = Drink.objects.get(id=pk)
    cart = Cart.objects.get(drink=drink)
    type = request.GET.get(drink.name)
    if type == '+':
        print("加入")
        cart.amount = cart.amount+1
        cart.save()
    else:
        print("減少")
        cart.amount = cart.amount-1
        cart.save()
    return redirect('cart')
    #return HttpResponse("Hello, world. You're at the polls index.")
