from datetime import timedelta
from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse
from django.utils.timezone import now

from users.models import EmailVerification, User


class UserRegisterViewTestCase(TestCase):
    """Класс для тестирования регистрации пользователя"""
    # Создайте свою fixture с социальным приложением
    # fixtures = ['socialapps.json']

    def setUp(self):
        """Объявляем нужные данные"""
        self.data = {
            'first_name': 'Mario', 'last_name': 'Super',
            'username': 'JumpMaster777', 'email': 'super_mario@example.com',
            'password1': '21Example_Pass12', 'password2': '21Example_Pass12',
        }
        self.path = reverse('users:register')

    def test_user_register_get(self):
        """Тест на отображение страницы"""
        response = self.client.get(self.path)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.context_data['title'], 'Store - Регистрация')
        self.assertTemplateUsed(response, 'users/register.html')

    def test_user_register_post(self):
        """Проверка на отправку данных от пользователя"""

        username = self.data['username']
        self.assertFalse(User.objects.filter(username=username).exists())
        response = self.client.post(self.path, self.data)

        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        # Для этого теста нужен объект социального приложения
        # self.assertRedirects(response, reverse('users:login'))
        self.assertTrue(User.objects.filter(username=username).exists())

        email_verification = EmailVerification.objects.filter(user__username=username)
        self.assertTrue(email_verification.exists())
        self.assertEqual(
            email_verification.first().expiration.date(),
            (now() + timedelta(hours=48)).date()
        )

    def test_user_register_post_error(self):
        """Проверка регистрации но с ошибкой"""
        User.objects.create(username=self.data['username'])
        response = self.client.post(self.path, self.data)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, 'Пользователь с таким именем уже существует.', html=True)
