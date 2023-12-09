from typing import Any
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from users.models import User, EmailVerification
from django import forms
import uuid
from datetime import timedelta
from django.utils.timezone import now


class UserLoginForm(AuthenticationForm):
    """Форма для авторизации"""
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите имя пользователя'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={  # PassInp скрывает вводимый текст
        'class': 'form-control py-4', 'placeholder': 'Введите пароль'}))

    class Meta:
        """С какой моделью форма работает и с какими полями"""
        model = User
        fields = ('username', 'password')


class UserRegisterForm(UserCreationForm):
    """Форма для регистрации"""
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите имя'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите фамилию'}))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите имя пользователя'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите адрес эл. почты'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Введите пароль'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control py-4', 'placeholder': 'Подтвердите пароль'}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')
        
    def save(self, commit: bool = True) -> Any:
        """Отправка эл. письма"""
        user = super(UserRegisterForm, self).save(commit=True)
        expiration = now() + timedelta(hours=48)
        record = EmailVerification.objects.create(code=uuid.uuid4(), user=user, expiration=expiration)
        record.send_verification_email()
        return user


class UserProfileForm(UserChangeForm):
    """Форма для личного кабинета пользователя"""
    first_name = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control py-4'}))
    last_name = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control py-4'}))
    image = forms.ImageField(required=False, widget=forms.FileInput(attrs={'class': 'custom-file-input'}))
    username = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'class': 'form-control py-4', 'readonly': True}))
    email = forms.CharField(required=False, widget=forms.EmailInput(
        attrs={'class': 'form-control py-4', 'readonly': True}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'image', 'username', 'email',)
