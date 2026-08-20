from django.contrib import admin
from products_app.models import Products, Category, Brand

# Register your models here.
admin.site.register(Products)
admin.site.register(Category)
admin.site.register(Brand)