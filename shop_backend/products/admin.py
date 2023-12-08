from django.contrib import admin
from products.models import ProductCategory, Product, Basket

admin.site.register(ProductCategory)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Класс для работы с товарами в админке"""
    list_display = ('name', 'price', 'quantity', 'category')
    fields = ('image', 'name', 'description', ('price', 'quantity'), 'category')
    search_fields = ('name',)
    ordering = ('name',)


class BasketAdmin(admin.TabularInline):
    """Отображение на странице пользователя"""
    model = Basket
    fields = ('product', 'quantity')
    readonly_fields = ('created_timestamp',)
    extra = 0
    