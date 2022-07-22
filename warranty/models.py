from django.db import models
from django_countries.fields import CountryField
from products.models import Product

class WarrantyRegistration(models.Model):
    
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    country = CountryField(blank_label='Country *', null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    products = models.ManyToManyField(Product)
    quantity = models.PositiveIntegerField(null=False)

    def __str__(self):
        return self.full_name

