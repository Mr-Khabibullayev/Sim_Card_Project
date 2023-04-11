from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    number = models.CharField(max_length=9)
    id = models.AutoField(primary_key=True)
    location = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=1000000000, decimal_places=1,default=0)
    
    def __str__(self) :
        return self.number
