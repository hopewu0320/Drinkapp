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
    
def cart(request):
    carts = Cart.objects.all()
    total = 0 
    for cart in carts:
        total+=cart.subtotal
    context = {'carts':carts,'total':total}
    return render(request, 'base/cart.html',context)

#更改購物車內容 增加 減少 刪除 清空購物車 
def editcart(request,pk):
    drink = Drink.objects.get(id=pk)
    cart = Cart.objects.get(drink=drink)
    type = request.GET.get(drink.name)
    if type == '+':
        print("加入")
        cart.amount = cart.amount+1
        cart.save()
    elif type=='-':
        print("減少")
        cart.amount = cart.amount-1
        cart.save()
    else:
        cart.delete()
    return redirect('cart')

#刪除購物車
def deletecart(request):
    Cart.objects.all().delete()
    return render(request, 'base/cart.html',{'total':0})

#送出訂單(應該要使用form)