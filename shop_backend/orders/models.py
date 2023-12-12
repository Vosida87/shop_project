from django.db import models

from users.models import User


class Order(models.Model):
    """Модель для работы с заказами"""
    CREATED = 0
    PAID = 1
    ON_WAY = 2
    DELIVERED = 3
    STATUSES = (
        (CREATED, 'Создан'),
        (PAID, 'Оплачен'),
        (ON_WAY, 'В пути'),
        (DELIVERED, 'Доставлен'),
    )
    # Может быть тот, кто инициализирует заказ и тот, кому пойдёт заказ
    first_name = models.CharField(max_length=64, verbose_name='Имя')
    last_name = models.CharField(max_length=64, verbose_name='Фамилия')
    email = models.EmailField(max_length=256, verbose_name='Почта')
    address = models.CharField(max_length=256, verbose_name='Адрес')
    basket_history = models.JSONField(default=dict, verbose_name='История о товарной корзине')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    status = models.SmallIntegerField(default=CREATED, choices=STATUSES, verbose_name='Статус заказа')
    initiator = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Инициатор заказа')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'Заказ №{self.id}. {self.first_name} {self.last_name}'
