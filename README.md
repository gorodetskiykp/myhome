# myhome

## Установка
1. python -m venv venv
2. venv\Scripts\activate (source venv/bin/activate)
3. pip install -r requirements.txt
   - pip install django
   - pip freeze > requirements.txt

## Настройка Django
1. django-admin startproject mytsrcn
   - manage.py - скрипт запуска
   - mytsrcn/ - каталог проекта
     - settings.py - настройки
       - INSTALLED_APPS - установленные приложения
       - ROOT_URLCONF - корневой роутер/маршрутизатор
       - TEMPLATES - html-шаблоны
       - DATABASES - работа с БД (DB Browser for SQLite)
       - STATIC_URL - место хранения img, css, js
     - urls.py - роутер/маршрутизатор
2. python manage.py createsuperuser
     
## Запуск проекта
1. python manage.py makemigrations
2. python manage.py migrate
3. python manage.py runserver

## Создание приложения
1. python manage.py startapp news
   - migrations/
   - admin.py - админка
   - apps.py - настройка приложения
   - models.py - модели
   - tests.py - тесты
   - views.py - views
2. Регистрация приложения в settings

## Обозначения
- ORM - python to DB
- MVC - model-view-controller
- MVCS - model-view-controller-service
- MTV - model-template-view
- FBV - functional based vies
- CBV - class based vies

## Клиент - сервер
- Browser -> [GET, POST] -> request
- Django -> urls -> view [models, template] -> response
