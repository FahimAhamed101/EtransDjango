from django.db import models
from store.models import Product
from accounts.models import Account
from django.core.validators import MinValueValidator, MaxValueValidator


    
# Create your models here.

class Carts(models.Model):
    carts_id = models.CharField(max_length=150,blank=True)
    date_added = models.DateTimeField(auto_now_add =True)
    coupon_applied =models.CharField(max_length=30,blank=True,null= True, default=0)
    final_offer_price =models.FloatField( blank=True, null=True , default = 0)
    user = models.EmailField(max_length=150,blank=True)




    def __str__(self):
        return self.carts_id

class CartItem(models.Model):
    size = (
        ('S', 'S'),
        ('M', 'M'),
        ('L', 'L')
    )
    user = models.ForeignKey(Account, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    cart = models.ForeignKey(Carts,on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField()
    is_active = models.BooleanField(default=True)
    size = models.CharField(max_length=10, choices=size, default='M', null = True )
    total = models.IntegerField(default=0, null = True )

    

    def item_total(self):
        return self.product.price * self.quantity


    def __str__(self):
        return self.product.product_name

class Coupon(models.Model):
    coupon_code = models.CharField(max_length=30,unique=True)
    valid_from = models.DateTimeField( null = True)
    valid_to = models.DateTimeField( null = True )
    discount = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(100)])
    active = models.BooleanField(default=True)
    def __str__(self):
        return self.coupon_code
    class  Meta:
        ordering = ['-valid_to',]
        


class Paymentrazor(models.Model):

    stat =  (("ACCEPTED", "ACCEPTED"), ("FAILED","FAILED"))


    payment_id = models.CharField(max_length=100, blank=True)
    order_id = models.CharField(max_length=100)
    payment_signature = models.CharField(max_length=100, blank=True)
    user = models.ForeignKey(Account,on_delete=models.CASCADE)
    total_amount = models.IntegerField()
    status = models.CharField(choices= stat, max_length=50,blank=True)