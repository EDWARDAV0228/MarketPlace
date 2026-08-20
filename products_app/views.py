from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from products_app.models import Products, Category, Brand


def main_page(request):

    products = Products.objects.all()


    search = request.GET.get('search')

    if search:
        products = products.filter(description__icontains=search).union(products.filter(category__name__icontains=search),
                                                                         products.filter(brand__name__icontains=search))


category = int(request.GET.get('category'))
    brand = int(request.GET.get('brand'))
    condition = request.GET.get('condition')


    print(f'Category: {category}\nBrand: {brand}\nCondition: {condition}')


    if not category and not brand and condition:
        return redirect('main_page')

    
    if category: 
        products = products.filter(category__id=category)
    if brand:
        products = products.filter(brand__id=brand)
    if condition:
        products = products.filter(condition=condition)


    page = request.GET.get('page', 1)
    page_size = request.GET.get('page_size', 4)

    paginator = Paginator(products, page_size)
    products = paginator.get_page(page)
    
    categories = Category.objects.all()
    brands = Brand.objects.all()

    return render(request, 'index.html', {'products': products, 'categories': categories, 'brands': brands, 'request': request,})

def get_product(request, product_id):
    try:
        product = Products.objects.get(id=product_id)
    except Products.DoesNotExist:
        return render(request, 'error.html')


    return render(request, 'product.html', {'product': product})

def cart_page(request):
    products = Products.objects.all

    return render(request, 'cart.html', {'products': products})

def filtration_products(request):


    products = Products.objects.all()
    

    search = request.GET.get('search')

    if search:
        products = products.filter(description__icontains=search).union(products.filter(category__name__icontains=search),
                                                                         products.filter(brand__name__icontains=search))


    page = request.GET.get('page', 1)
    page_size = request.GET.get('page_size', 4)

    paginator = Paginator(products, page_size)
    products = paginator.get_page(page)

    brands = Brand.objects.all()
    categories = Category.objects.all()


    return render(request, 'index.html', {'products': products, 'brands': brands, 'categories': categories, 'category_get': category, 'brand_get': brand, 'condition_get': condition,})

    