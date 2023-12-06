from django.shortcuts import render, HttpResponseRedirect
from users.forms import UserLoginForm, UserRegisterForm, UserProfileForm
from django.contrib import auth, messages
from django.urls import reverse
from products.models import Basket
from django.contrib.auth.decorators import login_required


def login(request):
    # Контроллер авторизации состоит из 3 этапов: Audit, Authentication, Authorization
    # Сначала происходит GET запрос серверу и показывается страница
    # Затем те данные которые заполнены пользователем в полях передаются серверу
    # POST - отправка данных, соответственно форма получает данные data = то что отдал пользователь
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():  # Далее полученные данные должны пройти валидацию
            username = request.POST['username']  # При прохождении валидации достаём нужные данные из словаря
            password = request.POST['password']
            user = auth.authenticate(request, username=username, password=password)  # Проверяем есть ли пользователь
            if user:  # Если пользователь есть
                auth.login(request, user)  # То он авторизуется
                return HttpResponseRedirect('/')  # и перенаправляется на главную
    else:  # Если метод запроса не является 'POST'
        form = UserLoginForm()  # создается пустой экземпляр формы UserLoginForm.
    # Затем создается контекст с формой и рендерится шаблон 'users/login.html' с использованием этого контекста.
    context = {'form': form}
    return render(request, 'users/login.html', context)


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            form.save()  # Вызываем метод save() для формы, который вызовет метод save() для объектов
            messages.success(request, 'Вак аккаунт успешно зарегистрирован!')
            return HttpResponseRedirect(reverse('users:login'))
    else:
        form = UserRegisterForm()
    context = {'form': form}
    return render(request, 'users/register.html', context)


@login_required
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(instance=request.user, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:register'))
    else:
        # Здесь необходимо передать данные уже и для GET запроса, чтобы они отображались в форме
        form = UserProfileForm(instance=request.user)  # передаём "экземпляр" пользователя, отправившего запрос
    
    context = {'title': 'Store - профиль',
               'form': form,
               'baskets': Basket.objects.filter(user=request.user),
               }
    return render(request, 'users/profile.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('products:index'))
