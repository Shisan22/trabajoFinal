from django.contrib import admin
from .models import Client, Product, Recipe, Location

# Register your models here.
admin.site.register(Client)
admin.site.register(Product)
admin.site.register(Recipe)
admin.site.register(Location)