from typing import Any

from django.contrib.auth.decorators import login_required
from django.core.cache import cache
from django.db.models.query import QuerySet
from django.shortcuts import HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView

from common.views import CommonMixin
from products.models import Basket, Product, ProductCategory


class IndexView(CommonMixin, TemplateView):
    """Отображение главной страницы"""
    template_name = 'products/index.html'
    title = 'Store'


class ProductsListView(CommonMixin, ListView):
    """Отвечает за отображение списка товаров"""
    model = Product
    template_name = 'products/products.html'
    paginate_by = 3
    title = 'Store - Каталог'

    def get_queryset(self) -> QuerySet[Any]:
        queryset = super(ProductsListView, self).get_queryset()
        category_id = self.kwargs.get('category_id')  # если не передан id, то вернёт None
        return queryset.filter(category_id=category_id) if category_id else queryset

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        categories = cache.get('categories')
        if not categories:
            context['categories'] = ProductCategory.objects.all()
            cache.set('categories', context['categories'], 30)
        else:
            context['categories'] = categories
        return context


@login_required
def basket_add(request, product_id):
    """Контроллер обработчик - добавить в корзину"""
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)

    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def basket_remove(request, basket_id):
    """Контроллер обработчик - убрать из корзины"""
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
