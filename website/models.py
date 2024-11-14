from django.db import models


class Client(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=14)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField()

class Recipe(models.Model):
    product = models.ForeignKey("Product", on_delete = models.CASCADE)
    image = models.ImageField()

class Location(models.Model):
    name = models.CharField(max_length=100)
    latitud = models.FloatField()
    longitud = models.FloatField()