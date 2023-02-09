from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Drink(models.Model):
    #user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True,blank=True)
    price = models.IntegerField(null=True)
    creadted = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    image = models.CharField(max_length=40, null=True,blank=False)
    def __str__(self):
        return self.name

class Cart(models.Model):
    drink = models.ForeignKey(Drink,on_delete=models.SET_NULL,null=True)
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    amount = models.IntegerField(null=True)
    subtotal = models.IntegerField(null=True)
    def __str__(self):
        return '{}{}杯'.format(self.drink.name ,self.amount)
    def save(self, *args, **kwargs):
        if self.amount < 1: #數量不能小於1
            self.amount = 1
        self.subtotal = self.drink.price * self.amount
        super(Cart, self).save(*args, **kwargs)
#Order 裡面要有Cart跟customer 每個Order搭配一個Cart, Cart裡面不需要有user
#customer要有user phone address