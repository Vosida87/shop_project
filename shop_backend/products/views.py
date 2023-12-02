from django.shortcuts import render

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
        'products': [
            {
                'image': '/static/src/img/products/Adidas-hoodie.png',
                'name': 'Худи черного цвета с монограммами adidas Originals',
                'price': 6090,
                'description': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.',
            },
            {
                'image': '/static/src/img/products/Blue-jacket-The-North-Face.png',
                'name': 'Синяя куртка The North Face',
                'price': 23725,
                'description': 'Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.',
            },
            {
                'image': '/static/src/img/products/Brown-sports-oversized-top-ASOS-DESIGN.png',
                'name': 'Коричневый спортивный oversized-топ ASOS DESIGN',
                'price': 3390,
                'description': 'Материал с плюшевой текстурой. Удобный и мягкий.',
            },
        ],
    }
    return render(request, 'products/products.html', context)
