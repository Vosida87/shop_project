from typing import Any
from users.forms import UserLoginForm, UserRegisterForm, UserProfileForm
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from products.models import Basket
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from users.models import User
from common.views import CommonMixin


class UserLoginView(CommonMixin, LoginView):
    """Авторизация пользователя"""
    template_name = 'users/login.html'
    form_class = UserLoginForm
    title = 'Store - Авторизация'
    
    def get_success_url(self) -> str:
        return reverse_lazy('products:index')


class UserRegisterView(SuccessMessageMixin, CommonMixin, CreateView):
    """Регистрация пользователя"""
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')
    success_message = 'Регистрация прошла успешно!'
    title = 'Store - Регистрация'
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super(UserRegisterView, self).get_context_data(**kwargs)
        return context


class UserProfileView(CommonMixin, UpdateView):
    """Личный кабинет пользователя"""
    model = User
    form_class = UserProfileForm
    template_name = 'users/profile.html'
    title = 'Store - Личный кабинет'
    
    def get_success_url(self) -> str:
        return reverse_lazy('users:profile', args=(self.object.id,))
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super(UserProfileView, self).get_context_data(**kwargs)
        context['baskets'] = Basket.objects.filter(user=self.object)
        return context


class UserLogoutView(LogoutView):
    """Sign out пользователя"""
    next_page = reverse_lazy('products:index')
