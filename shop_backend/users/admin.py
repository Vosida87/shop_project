from django.contrib import admin
from users.models import User
from products.admin import BasketAdmin


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Класс для работы с пользователями в админке"""
    list_display = ('username',)
    inlines = (BasketAdmin,)
