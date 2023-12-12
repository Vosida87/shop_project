from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse

from products.models import Product, ProductCategory


class IndexViewTestCase(TestCase):
    """Тест на посещение главной страницы"""
    def test_view(self):
        """Проверка представления"""
        path = reverse('products:index')
        response = self.client.get(path)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.context_data['title'], 'Store')
        self.assertTemplateUsed(response, 'products/index.html', 'products/base.html')


class ProductsListViewTestCase(TestCase):
    """Тест на посещение страницы с товарами"""
    fixtures = ['categories.json', 'products.json']

    def setUp(self):
        """Объявляем нужные данные"""
        self.products = Product.objects.all()

    def _common_tests(self, response):
        """Шаблон для тестов"""
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.context_data['title'], 'Store - Каталог')
        self.assertTemplateUsed(response, 'products/products.html', 'products/base.html')

    def test_list(self):
        """Проверка отображения товаров"""
        path = reverse('products:list')
        response = self.client.get(path)

        self._common_tests(response)
        self.assertEqual(list(response.context_data['object_list']), list(self.products[:3]))

    def test_list_with_category(self):
        """Проверка отображения товаров выбранной категории"""
        category = ProductCategory.objects.first()
        path = reverse('products:category', kwargs={'category_id': category.id})
        response = self.client.get(path)

        self._common_tests(response)
        self.assertEqual(
            list(response.context_data['object_list']),
            list(self.products.filter(category_id=category.id)[:3])
            )
