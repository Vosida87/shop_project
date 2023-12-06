from django.shortcuts import render, HttpResponseRedirect
from products.models import ProductCategory, Product, Basket
from users.models import User
from django.contrib.auth.decorators import login_required


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


@login_required
def basket_add(request, product_id):
    """Контроллер обработчик - добавить в корзину"""
    product = Product.objects.get(id=product_id)  # Забирает id товара, который выбрал user
    #  далее фильтрация на то, что корзина только пользователя и его товар
    #  если товара нет, то он добавится, если есть, то увеличится
    baskets = Basket.objects.filter(user=request.user, product=product)
    
    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()
    # возвращаем на ту же страницу, с которой поступил запрос
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
