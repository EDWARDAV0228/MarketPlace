from django.urls import path
from .views import * 

urlpatterns = [
    path('', main_page, name='main_page'),
    path('product/<int:product_id>', get_product, name='product_page'),
    path('cart/', cart_page, name='cart_page'),  
]