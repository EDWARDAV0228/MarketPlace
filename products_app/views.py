from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from products_app.forms import ProductForms
from products_app.models import Products, Category, Brand, ImageGallery, ProductLinks


def main_page(request):

    products = Products.objects.all()
    categories = request.GET.getlist("category_check")
    brands = request.GET.getlist("brand_check")
    conditions = request.GET.get("condition_check")
    to_price = request.GET.get("to_price")
    from_price = request.GET.get("from_price")
    sort_type = request.GET.get("sort")

    search = request.GET.get("search")

    if search:
        products = products.filter(description__icontains=search).union(
            products.filter(category__name__icontains=search),
            products.filter(brand__name__icontains=search),
        )

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
            if condition == "1":
                products = products.filter(condition="Б-У")
            if condition == "2":
                products = products.filter(condition="Новое")

    if sort_type:
        match sort_type:
            case "name_1":
                products = products.order_by("name")
            case "name_1":
                products = products.order_by("-name")
            case "category_1":
                products = products.order_by("category")
            case "category_2":
                products = products.order_by("-category")
            case "brand_1":
                products = products.order_by("brand")
            case "brand_2":
                products = products.order_by("-brand")
            case "price_1":
                products = products.order_by("price")
            case "price_2":
                products = products.order_by("-price")

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

    form = ProductForms()

    if request.method == "POST":
        form = ProductForms(data=request.POST, files=request.FILES)
        if form.is_valid():
            product = form.save()
            return redirect("workspace")

    return render(request, "workspace/create.html", {"form": form})


def del_product(request, product_id):
    product = get_object_or_404(Products, pk=product_id)
    product.delete()
    return redirect("workspace")


def edit_product(request, product_id):
    product = get_object_or_404(Products, pk=product_id)
    form = ProductForms(instance=product)

    if request.method == "POST":
        form = ProductForms(instance=product, data=request.POST, files=request.FILES)
        if form.is_valid():
            product = form.save()
            return redirect("workspace")

    return render(request, "workspace/edit.html", {"product": product, "form": form})
