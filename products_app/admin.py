from django.contrib import admin
from django.utils.safestring import mark_safe
from products_app.models import Products, Category, Brand, ImageGallery


class ImageGalleryInline(admin.TabularInline):
    model = ImageGallery
    extra = 0
    readonly_fields = ("created_date", "get_image")

    @admin.display(description="Изображение")
    def get_image(self, obj: ImageGallery):
        if obj.file:
            return mark_safe(f'<img src="{obj.file.url}" width="100px">')


@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "price",
        "brand",
        "category",
        "date",
        "display_image",
    )
    list_display_links = ("name",)
    list_filter = (
        "category",
        "brand",
    )
    readonly_fields = ("date", "ubdate_date", "views")
    search_fields = ("name",)
    inlines = (ImageGalleryInline,)

    def display_image(self, obj):
        if obj and obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="100px">')
        return "Нет изображения"

    display_image.short_description = "Изображение"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "display_image")
    list_display_links = ("name",)
    readonly_fields = ("display_image",)
    search_fields = (
        "id",
        "name",
    )

    def display_image(self, obj):
        if obj and obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="100px">')
        return "Нет изображения"

    display_image.short_description = "Изображение"


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
    )
    list_display_links = ("name",)
    search_fields = (
        "id",
        "name",
    )
