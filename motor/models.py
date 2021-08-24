from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=150)
    sku = models.CharField(max_length=150, unique=True)
    price = models.FloatField()
    brand = models.CharField(max_length=150)
    description = models.TextField()
    img = models.ImageField(upload_to='images')
    quantity = models.IntegerField()
    slug = models.SlugField()
    consulted = models.IntegerField()
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.name
