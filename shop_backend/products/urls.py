from products.apps import ProductsConfig
from django.urls import path
from products.views import index, products, basket_add, basket_remove

app_name = ProductsConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('products/', products, name='list'),
    path('products/basket/add/<int:product_id>/', basket_add, name='basket_add'),
    path('products/basket/remove/<int:basket_id>/', basket_remove, name='basket_remove'),
]
