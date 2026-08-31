from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from products_app.models import Products, Category, Brand


def main_page(request):

    products = Products.objects.all()
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

    categories = Category.objects.all()
    brands = Brand.objects.all()

    return render(
        request,
        "index.html",
        {
            "products": products,
            "brands": brands,
            "categories": categories,
            "category_get": category,
            "brand_get": brand,
        },
    )


def get_product(request, product_id):
    try:
        product = Products.objects.get(id=product_id)
    except Products.DoesNotExist:
        return render(request, "error.html")

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

    categories = Category.objects.all()
    brands = Brand.objects.all()

    return render(
        request,
        "cart.html",
        {
            "products": products,
            "brands": brands,
            "categories": categories,
            "category_get": category,
            "brand_get": brand,
        },
    )


def workspace(request):

    products = Products.objects.all()

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
        full_description = request.POST.get("full-description")
        price = request.POST.get("price")
        author = request.POST.get("author")
        category = Category.objects.get(id=int(request.POST.get("category")))
        brand = Brand.objects.get(id=int(request.POST.get("brand")))
        model = request.POST.get("model")

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

        if image:
            product.image.save(image.name, image)

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
        product.full_description = request.POST.get("full-description")
        product.price = request.POST.get("price")
        product.author = request.POST.get("author")
        product.category = Category.objects.get(id=int(request.POST.get("category")))
        product.brand = Brand.objects.get(id=int(request.POST.get("brand")))
        product.model = request.POST.get("model")

        if image:
            product.image.save(image.name, image)

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
