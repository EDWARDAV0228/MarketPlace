from django.contrib import admin
from django.utils.safestring import mark_safe
from products_app.models import Products, Category, Brand




@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'brand', 'category', 'date', 'ubdate_date',)
    list_display_links = ('name',)
    list_filter = ('category', 'brand',)
    readonly_fields = ('date', 'ubdate_date')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    
    def display_image(self, obj):
        if obj and obj.image:
            return mark_safe(f'<img src"{obj.image.url}" width="100px">')
        return 'Нет изображения'

    display_image.short_description = 'Изображение товара'
    list_display_links = ('name',)
    

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_display_links = ('name',)

    