from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Drink,Cart,Customer
from django.contrib.auth.decorators import login_required
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
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        if form.is_valid():
           user = form.save(commit=False)  #回傳一個user object
           user.username = user.username.lower()
           user.save()
           Customer.objects.create(user=user,phone=phone,address=address)
           print("fgdfgdfgdf")
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
@login_required(login_url='login')
def addtocart(request,pk):    
    drink = Drink.objects.get(id=pk)
    customer = Customer.objects.get(user=request.user)
    if request.method == "POST":
        if Cart.objects.filter(customer=customer,drink=drink).exists(): #從Cart往Customer再往User找到object
            cart = Cart.objects.get(customer=customer,drink=drink)
            cart.amount = cart.amount+1
            cart.save()
        else:
            Cart.objects.create(
            drink = drink,
            amount = 1,
            customer = customer,
            subtotal = 0,
            )  
        return redirect('cart')
@login_required(login_url='login')   
def cart(request):
    customer = Customer.objects.get(user=request.user)
    carts = Cart.objects.filter(customer=customer) #回傳hope 玫瑰茶一杯 晚安茶一杯
    total = 0 
    for cart in carts:
        total+=cart.subtotal
    context = {'carts':carts,'total':total}
    return render(request, 'base/cart.html',context)

#更改購物車內容 增加 減少 刪除 清空購物車 
def editcart(request,pk):
    drink = Drink.objects.get(id=pk)
    customer = Customer.objects.get(user=request.user)
    cart = Cart.objects.get(customer=customer,drink=drink)  #指定兩種屬性 因為hope 跟hopewu1都有玫瑰茶
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
    customer = Customer.objects.get(user=request.user)
    Cart.objects.filter(customer=customer).delete()  #hope的購物車所有東西刪除
    return render(request, 'base/cart.html',{'total':0})

def cart_order(request):
    pass
    context = {}
    return render(request, 'base/order.html',context)


    