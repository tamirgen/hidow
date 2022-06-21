from django.db import models
from django.utils import timezone

# Create your models here.

class Products(models.Model):

    class Meta:
        verbose_name_plural = 'Products'

    name = models.CharField(default='', max_length=254)
    description = models.TextField()
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    productId=models.BigIntegerField(default=0) 

    def __str__(self):
        return self.name
    

class Review(models.Model):
    author = models.CharField(max_length=40, default="anonymous")
    review_date = models.DateTimeField(default=timezone.now)
    rate_choices = (
        (1,1),
        (2,2),
        (3,3),
        (4,4),
        (5,5)
    )
    stars = models.IntegerField(choices=rate_choices)
    comment = models.TextField(max_length=4000)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)

    def __str__(self):
        return self.product.name

