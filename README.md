# Технологии
[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat-square&logo=Django)](https://www.djangoproject.com/)
[![Django REST Framework](https://img.shields.io/badge/-Django%20REST%20Framework-464646?style=flat-square&logo=Django%20REST%20Framework)](https://www.django-rest-framework.org/)
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?style=flat-square&logo=PostgreSQL)](https://www.postgresql.org/)
[![Nginx](https://img.shields.io/badge/-NGINX-464646?style=flat-square&logo=NGINX)](https://nginx.org/ru/)
[![gunicorn](https://img.shields.io/badge/-gunicorn-464646?style=flat-square&logo=gunicorn)](https://gunicorn.org/)
[![docker](https://img.shields.io/badge/-Docker-464646?style=flat-square&logo=docker)](https://www.docker.com/)

# Продуктовый помощник
Foodgram - социальная сеть для любителей вкусного, где можно публиковать свои рецепты, подписываться на других кулинаров, добавлять шедевры в избранное, а также формировать список покупок для приготовления всех выбранных блюд.

# Запуск проекта в контейнерах Docker
### Клонируйте репозиторий на свой компьютер
#### HTTPS
```
git clone https://github.com/AleksSpace/foodgram-project-react.git
```
#### SSH
```
git clone git@github.com:AleksSpace/foodgram-project-react.git
```
### Создайте и активируйте виртуальное окружение
```
cd название_проекта/backend/
python -m venv venv
source venv/bin/activate
```
### Установите зависимостси
```
python -m venv venv
```
```
pip install -r requirements.txt
```
## Создайте файл .env
С помощью команды cd перейдите в папку infra 
```
touch .env
```
Заполните файл, пример ниже:
```
SECRET_KEY=some-secret-key
ALLOWED_HOSTS=*
DEBUG=True
DB_ENGINE=django.db.backends.postgresql 
DB_NAME=postgres
POSTGRES_USER=<...> 
POSTGRES_PASSWORD=<...>
DB_HOST=<...> 
DB_PORT=<...> 
```
## Сборка и запуск контейнеров
Установите приложение [Docker](https://www.docker.com/products/docker-desktop/) на свой ПК.
#### Отредактируйте файл docker-compose.yml
```
backend:
    build:
      context: ../backend
      dockerfile: Dockerfile
    volumes:
      - static_backend_value:/code/static_backend/
      - media_data:/code/media/
    depends_on:
      - db
    env_file:
      - ./.env
```
```
frontend:
    build:
      context: ../frontend
      dockerfile: Dockerfile
    volumes:
      - ../frontend/:/app/result_build/
    depends_on:
      - backend
```
#### Для запуска из DockerHub необходимо в файле docker-compose.yml указать имя пользователя и название репозитория
Перейдите в папку infra и отредактируйте файл, в разделе web:
```
backend:
    image: <Имя пользователя>/<Название репозитория>
    volumes:
      - static_backend_value:/code/static_backend/
      - media_data:/code/media/
    depends_on:
      - db
    env_file:
      - ./.env
```
```
frontend:
    image: <Имя пользователя>/<Название репозитория>
    volumes:
      - ../frontend/:/app/result_build/
    depends_on:
      - backend
```
### Сборка контейенеров
Перейдите в папку infra

```
docker compose up -d
```
#### Создайте суперпользователя
```
docker compose exec web python manage.py createsuperuser
```

### Заполнение базы данных
Заполните БД подготовленными данными при первом запуске

``` 
docker compose exec web python manage.py loaddata fixtures/ingredients_to_load.json
```
Чтобы сформировать ingredients_to_load.json можно запустить скрипт prepare_data
***
## Проект будет доступен по ссылке:

API - http://localhost/

Redoc - http://localhost/api/docs/

Панель администратора - http://localhost/admin/


## Deploy на сервер
При пуше в ветку master выполняется автоматическое разворачивание проекта на сервере при заполнении секретов в гитхабе в данном репозитории
***
### Об авторе
- Ганецкая Елизавета - backend и deploy
