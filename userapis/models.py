from django.db import models
from django.contrib.auth.models import User

class Books(models.Model):
    id = models.IntegerField(primary_key=True,null=False)
    name=models.CharField(max_length=100, null=False)
    author = models.CharField(max_length=100, null=False)
    price=models.IntegerField(null=False)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
   
    first_name = models.CharField(max_length=200)
    address = models.CharField(max_length=500)
    
    def __str__(self):
        return self.user.username if self.user else "No user"
    
    





# Create your models here.
