from django.db import models

NULLABLE = {'null': True, 'blank': True}  # Можно оставлять поле незаполненным


class ProductCategory(models.Model):
    """Модель категорий товаров"""
    name = models.CharField(max_length=128, unique=True, verbose_name='Название категории')
    description = models.TextField(**NULLABLE, verbose_name='Описание категории')
    # Для сохранения в БД
    # category = ProductCategory(name='одежда') - обычное создание экземпляра
    # category.save() - далее для сохранения в БД
    # QuerySet - набор запросов, который представляет собой набор объектов из базы данных
    # или ProductCategory.objects.create() (QuerySet методы - create() / get() / all() / filter() и другие)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return f'Категория: {self.name}'


class Product(models.Model):
    """Модель товаров"""
    name = models.CharField(max_length=256, verbose_name='Название товара')
    description = models.TextField(verbose_name='Описание товара')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    quantity = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='products_images')
    # cascade - удалим категорию - удалятся и товары, protect - пока не удалим товары не удалится и категория
    # set_default - если удалится категория, то поставится значение по умолчанию default=
    category = models.ForeignKey(to=ProductCategory, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return f'Название: {self.name}, Категория: {self.category.name}'
