from products.apps import ProductsConfig
from django.urls import path
from products.views import index, products

app_name = ProductsConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('products/', products, name='list'),
]
