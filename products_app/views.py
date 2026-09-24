from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.db import IntegrityError
from products_app.models import Products, Category, Brand, ImageGallery, ProductLinks


def main_page(request):

    products = Products.objects.all()
    categories = request.GET.getlist("category_check")
    brands = request.GET.getlist("brand_check")
    conditions = request.GET.get("condition_check")
    to_price = request.GET.get("to_price")
    from_price = request.GET.get("from_price")

    search = request.GET.get("search")

    if search:
        products = products.filter(description__icontains=search).union(
            products.filter(category__name__icontains=search),
            products.filter(brand__name__icontains=search),
        )

    # if (
    #     not categories
    #     and not brands
    #     and not conditions
    #     # and not from_price
    #     # and not to_price
    # ):
    #     return redirect("main_page")

    if from_price and not to_price:
        products = products.filter(price__gte=from_price)

    if to_price and not from_price:
        products = products.filter(price__lte=to_price)

    if to_price and from_price:
        products = products.filter(price__gte=from_price, price__lte=to_price)

    if categories:
        products = products.filter(category__id__in=categories)
    if brands:
        products = products.filter(brand__id__in=brands)
    if conditions:
        for condition in conditions:
            if condition == '1':
                products = products.filter(condition='Б-У')
            if condition == '2':
                products = products.filter(condition='Новое')
    

    page = request.GET.get("page", 1)
    page_size = request.GET.get("page_size", 9)

    paginator = Paginator(products, page_size)
    products = paginator.get_page(page)

    return render(
        request,
        "index.html",
        {
            "products": products,
        },
    )


def get_product(request, product_id):
    try:
        product = Products.objects.get(id=product_id)
    except Products.DoesNotExist:
        return render(request, "error.html")

    product.views += 1
    product.save()

    return render(request, "product.html", {"product": product})


def cart_page(request):
    products = Products.objects.all

    category = request.GET.get("category")
    brand = request.GET.get("brand")
    condition = request.GET.get("condition")

    search = request.GET.get("search")

    if search:
        products = products.filter(description__icontains=search).union(
            products.filter(category__name__icontains=search),
            products.filter(brand__name__icontains=search),
        )

    if not category and not brand and condition:
        return redirect("main_page")

    if category:
        products = products.filter(category__id=category)
        category = int(category)
    if brand:
        products = products.filter(brand__id=brand)
        brand = int(brand)
    if condition:
        products = products.filter(condition=condition)

    page = request.GET.get("page", 1)
    page_size = request.GET.get("page_size", 4)

    paginator = Paginator(products, page_size)
    products = paginator.get_page(page)

    return render(
        request,
        "cart.html",
        {
            "products": products,
            "category_get": category,
            "brand_get": brand,
        },
    )


def workspace(request):

    products = Products.objects.all()

    search = request.GET.get("search")

    if search:
        products = products.filter(description__icontains=search).union(
            products.filter(category__name__icontains=search),
            products.filter(brand__name__icontains=search),
        )

    page = request.GET.get("page", 1)
    page_size = request.GET.get("page_size", 4)

    paginator = Paginator(products, page_size)
    products = paginator.get_page(page)

    categories = Category.objects.all()
    brands = Brand.objects.all()

    return render(
        request,
        "workspace/index.html",
        {
            "products": products,
            "brands": brands,
            "categories": categories,
        },
    )


def create_product(request):

    if request.method == "POST":
        name = request.POST.get("product-name")
        description = request.POST.get("description")
        image = request.FILES.get("image")
        gallery = request.FILES.getlist("gallery")
        full_description = request.POST.get("full-description")
        price = request.POST.get("price")
        author = request.POST.get("author")
        category = Category.objects.get(id=int(request.POST.get("category")))
        brand = Brand.objects.get(id=int(request.POST.get("brand")))
        model = request.POST.get("model")
        whatsapp = request.POST.get("whatsapp")
        telegram = request.POST.get("telegram")
        instagram = request.POST.get("instagram")
        facebook = request.POST.get("facebook")

        product = Products.objects.create(
            name=name,
            description=description,
            full_description=full_description,
            price=price,
            author=author,
            category=category,
            brand=brand,
            model=model,
        )

        ProductLinks.objects.create(
            product=product,
            whatsapp=whatsapp,
            telegram=telegram,
            instagram=instagram,
            facebook=facebook,
        )

        if image:
            product.image.save(image.name, image)

        if gallery:
            for img in gallery:
                image = ImageGallery.objects.create(
                    product=product,
                    file=img,
                )

        product.save()

        return redirect("workspace")

    categoryes = Category.objects.all()
    brands = Brand.objects.all()

    return render(
        request,
        "workspace/create.html",
        {
            "categoryes": categoryes,
            "brands": brands,
        },
    )


def del_product(request, product_id):
    product = get_object_or_404(Products, pk=product_id)
    product.delete()
    return redirect("workspace")


def edit_product(request, product_id):
    product = get_object_or_404(Products, pk=product_id)
    if request.method == "POST":
        product.name = request.POST.get("product-name")
        product.description = request.POST.get("description")
        image = request.FILES.get("image")
        gallery = request.FILES.getlist("gallery")
        product.full_description = request.POST.get("full-description")
        product.price = request.POST.get("price")
        product.author = request.POST.get("author")
        product.category = Category.objects.get(id=int(request.POST.get("category")))
        product.brand = Brand.objects.get(id=int(request.POST.get("brand")))
        product.model = request.POST.get("model")
        whatsapp = request.POST.get("whatsapp")
        telegram = request.POST.get("telegram")
        instagram = request.POST.get("instagram")
        facebook = request.POST.get("facebook")

        ProductLinks.objects.update_or_create(
            product=product,
            defaults={
                "whatsapp": whatsapp,
                "telegram": telegram,
                "instagram": instagram,
                "facebook": facebook,
            },
        )
        if image:
            product.image.save(image.name, image)

        if gallery:
            for img in gallery:
                ImageGallery.objects.create(product=product, file=img)

        product.save()
        return redirect("workspace")

    categoryes = Category.objects.all()
    brands = Brand.objects.all()

    return render(
        request,
        "workspace/edit.html",
        {
            "product": product,
            "categoryes": categoryes,
            "brands": brands,
        },
    )
