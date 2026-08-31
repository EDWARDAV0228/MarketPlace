from django.contrib import admin
from django.utils.safestring import mark_safe
from products_app.models import Products, Category, Brand




@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'brand', 'category', 'date', 'display_image',)
    list_display_links = ('name',)  
    list_filter = ('category', 'brand',)
    readonly_fields = ('date', 'ubdate_date')
    search_fields = ('name',)

    def display_image(self, obj):
        if obj and obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="100px">')
        return 'Нет изображения'
    
    display_image.short_description = 'Изображение'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'display_image')
    list_display_links = ('name',)
    readonly_fields = ('display_image',)

    def display_image(self, obj):
        if obj and obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="100px">')
        return 'Нет изображения'
    
    display_image.short_description = 'Изображение'
    

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_display_links = ('name',)

    