from products.apps import ProductsConfig
from django.urls import path
from products.views import IndexView, ProductsListView, basket_add, basket_remove

app_name = ProductsConfig.name

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('products/', ProductsListView.as_view(), name='list'),
    path('products/category/<int:category_id>/', ProductsListView.as_view(), name='category'),
    path('products/page/<int:page>/', ProductsListView.as_view(), name='paginator'),
    path('products/basket/add/<int:product_id>/', basket_add, name='basket_add'),
    path('products/basket/remove/<int:basket_id>/', basket_remove, name='basket_remove'),
]
