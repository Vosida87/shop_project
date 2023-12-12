# `shop_project`
Shop project - это онлайн магазин, разработанный с использованием Django framework.  
Стек: `Python`, `Django`, `DjangoTemplates`, `PostgreSql`, `OAuth 2.0`, `flake8`, `isort`
***
## `Описание`
Проект магазина предоставляет следующие функции:
- Регистрация и аутентификация пользователей (в том числе через GitHub с помощью OAuth 2.0);
- Рассылка электронной почты для подтверждения аккаунта;
- Редактирование профиля пользователя в личном кабинете;
- Просмотр доступных товаров;
- Добавление товаров в корзину;
- Расчет общей стоимости товаров в корзине;
***
## `Установка и запуск проекта`
1. Клонируйте проект на ваш локальный компьютер `git clone <URL-repo>`;
2. Создайте и активируйте виртуальное окружение для проекта `python -m venv venv`, `vens/Scripts/activate`;
3. Установите необходимые зависимости `pip install -r requirements.txt`;
4. Создайте базу данных для проекта `psql -U postgres` (postgres - имя пользователя), `CREATE DATABASE <DB_NAME>;`;
5. Заполните файл `.env_example` (переименуйте его в .env);
6. Выполните миграции `python manage.py migrate`;
7. Для создания авторизации через GitHub, нужно зарегистрировать его на гитхабе и в админке проекта;
8. Загрузите фикстуры `python manage.py loaddata <fixture_name>`;
9. Проверка тестов `python manage.py test`;
10. Запуск `python manage.py runserver`;
11. Откройте веб-браузер и перейдите по адресу `http://localhost:8000` для просмотра проекта.
***
## `Используемые технологии`
- `Django` - основной фреймворк для разработки проекта;
- `Django-allauth` - библиотека для протокла OAuth 2.0;
- `HTML, CSS, JavaScript` - для разработки пользовательского интерфейса и взаимодействия с клиентом.
