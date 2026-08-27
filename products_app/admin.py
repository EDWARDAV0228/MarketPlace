from django.contrib import admin
from products_app.models import Products, Category, Brand




@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'brand', 'category', 'date', 'ubdate_date',)
    list_display_links = ('name',)
    list_filter = ('category', 'brand',)
    readonly_fields = ('date', 'ubdate_date')


admin.site.register(Category)
admin.site.register(Brand)