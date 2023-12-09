from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.mail import send_mail
from django.db import models
from django.urls import reverse
from django.utils.timezone import now

NULLABLE = {'null': True, 'blank': True}


class User(AbstractUser):
    """Расширяем модель пользователя"""
    image = models.ImageField(upload_to='users_image', **NULLABLE, verbose_name='Аватарка')
    is_verified_email = models.BooleanField(default=False, verbose_name='Подтвердил ли почту')

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class EmailVerification(models.Model):
    """Проверка Email"""
    code = models.UUIDField(unique=True, verbose_name='Уникальная ссылка')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    expiration = models.DateTimeField(verbose_name='Срок действия')

    def __str__(self) -> str:
        return f'EmailVerification для {self.user.email}'

    class Meta:
        verbose_name = 'Email проверка'
        verbose_name_plural = 'Email проверки'

    def send_verification_email(self):
        """Отправка проверочного письма"""
        link = reverse('users:verify',
                       kwargs={'email': self.user.email,
                               'code': self.code,
                               }
                       )
        verification_link = f'{settings.DOMAIN_NAME}{link}'
        subject = f'Подтверждение учётной записи для {self.user.username}'
        message = 'Для подтверждения учётной записи для {} перейдите по ссылке: {}'.format(
            self.user.username,
            verification_link
        )
        send_mail(
            subject=subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[self.user.email],
            fail_silently=False,
        )

    def is_expired(self):
        """Проверяет не истёк ли срок действия ссылки"""
        return True if now() >= self.expiration else False
