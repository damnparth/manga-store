from django.db import models
from django.contrib.auth.models import User

class Books(models.Model):
    id = models.IntegerField(primary_key=True,null=False)
    name=models.CharField(max_length=100, null=False)
    author = models.CharField(max_length=100, null=False)
    price=models.IntegerField(null=False)

class Cart(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE) #cuz one cart for one user

class CartItem(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE,null=True) #why cartItem? we already storing books na? ANS: cartItem makes it easier to handle quantities
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
    book=models.ForeignKey(Books,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)



class Profile(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)   
    first_name = models.CharField(max_length=200, blank=True, null=True)
    address = models.CharField(max_length=500,blank=True, null=True)
    
    def __str__(self):
        return self.user.username 
    
    





# Create your models here.
