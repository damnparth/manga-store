from django.db import models

class Books(models.Model):
    id = models.IntegerField(primary_key=True,null=False)
    name=models.CharField(max_length=100, null=False)
    author = models.CharField(max_length=100, null=False)

class Profile(models.Model):
    first_name=models.CharField(primary_key=True, null=False, max_length=200)
    address=models.CharField(null=False,max_length=500)
    
   
    






# Create your models here.
