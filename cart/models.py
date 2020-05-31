from django.db import models
from django.conf import settings
from mamazon.models import Product

User = settings.AUTH_USER_MODEL

class Cart(models.Model):
    user = models.models.ForeignKey(User, null=True, blank=True, on_delate=CASCADE)
    products = models.models.ManyToManyField(Product, blank=True)
    total = models.models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    created = models.models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
