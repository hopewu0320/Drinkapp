from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Drink,Cart
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import (
    authenticate,
    login,
    logout,
)

def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request,'Invalid User!')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,'Username or password is incorrect!')
    context={'page':page}
    return render(request, 'base/login_register.html',context)
def registerPage(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
           user = form.save(commit=False)  #回傳一個user object
           user.username = user.username.lower()
           user.save()
           login(request,user)
           return redirect('home')
        else:
            messages.error(request,"Invalid registration!") 
    context = {'form':form}
    return render(request, 'base/login_register.html',context)
def logoutUser(request):
    logout(request)
    return redirect('home')
def home(request):
    drinks = Drink.objects.all()
    context = {'drinks':drinks}
    return render(request, 'base/home.html',context)

def productinfo(request,pk):
    drink = Drink.objects.get(id=pk)
    context = {'drink':drink}
    return render(request, 'base/productinfo.html',context)


#目前問題:加入購物車,要知道目前的使用者是誰
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
            user = request.user,
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
