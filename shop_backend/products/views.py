from django.shortcuts import render
from products.models import ProductCategory, Product

# def index(request):
#     """Представление в которое передаётся запрос-request, и view отвечает response-Hello there!"""
#     return HttpResponse('Hello there!')

# def index(request):
#     """
#     Также для взаимодействия запроса с шаблоном используем render,
#     можно передавать context (данные в виде словаря), и с ним работать в шаблоне (доставать оттуда нужные значения)
#     """
#     return render(request, 'products/test.html', {'title': 'Test'})


def index(request):
    context = {
        'title': 'Store',
    }
    return render(request, 'products/index.html', context)


def products(request):
    context = {
        'title': 'Store - каталог',
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all(),
    }
    return render(request, 'products/products.html', context)
