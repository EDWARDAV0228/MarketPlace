from django.urls import path
from .views import * 

urlpatterns = [
    path('', main_page, name='main_page'),
    path('product/<int:product_id>', get_product, name='product_page'),
    path('cart/', cart_page, name='cart_page'),  
    path('workspace', workspace, name='workspace'),
    path('workspace/create', create_product, name='create_product'),
    path('workspace/del/<int:product_id>', del_product, name='del_product'),
    path('workspace/edit/<int:product_id>', edit_product, name='edit_product')
]