from django.shortcuts import render
from django.http import HttpResponse
from .models import Drink
# Create your views here.

def home(request):
    context = {}
    return render(request, 'base/home.html',context)

def productinfo(request,pk):
    drink = Drink.objects.all()
    context = {'drink':drink}
    return render(request, 'base/productinfo.html',context)