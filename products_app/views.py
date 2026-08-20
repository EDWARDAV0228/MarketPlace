from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from products_app.models import Products, Category, Brand


def main_page(request):

    products = Products.objects.all()
    category = request.GET.get('category')
    brand = request.GET.get('brand')
    condition = request.GET.get('condition')


    search = request.GET.get('search')

    if search:
        products = products.filter(description__icontains=search).union(products.filter(category__name__icontains=search),
                                                                         products.filter(brand__name__icontains=search))



    if not category and not brand and condition:
        return redirect('main_page')

    
    if category: 
        products = products.filter(category__id=category)
        category = int(category)
    if brand:
        products = products.filter(brand__id=brand)
        brand = int(brand)
    if condition:
        products = products.filter(condition=condition)


    page = request.GET.get('page', 1)
    page_size = request.GET.get('page_size', 4)

    paginator = Paginator(products, page_size)
    products = paginator.get_page(page)
    
    categories = Category.objects.all()
    brands = Brand.objects.all()

    return render(request, 'index.html', {'products': products, 'brands': brands, 'categories': categories, 'category_get': category, 'brand_get': brand, 'condition_get': condition,})


def get_product(request, product_id):
    try:
        product = Products.objects.get(id=product_id)
    except Products.DoesNotExist:
        return render(request, 'error.html')


    return render(request, 'product.html', {'product': product})

def cart_page(request):
    products = Products.objects.all

    return render(request, 'cart.html', {'products': products})
