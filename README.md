![foodgram workflow](https://github.com/DmitryTok/foodgram-project-react/actions/workflows/main.yml/badge.svg)
[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat-square&logo=Django)](https://www.djangoproject.com/)
[![Django REST Framework](https://img.shields.io/badge/-Django%20REST%20Framework-464646?style=flat-square&logo=Django%20REST%20Framework)](https://www.django-rest-framework.org/)
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?style=flat-square&logo=PostgreSQL)](https://www.postgresql.org/)
[![Nginx](https://img.shields.io/badge/-NGINX-464646?style=flat-square&logo=NGINX)](https://nginx.org/ru/)
[![gunicorn](https://img.shields.io/badge/-gunicorn-464646?style=flat-square&logo=gunicorn)](https://gunicorn.org/)
[![docker](https://img.shields.io/badge/-Docker-464646?style=flat-square&logo=docker)](https://www.docker.com/)
[![GitHub%20Actions](https://img.shields.io/badge/-GitHub%20Actions-464646?style=flat-square&logo=GitHub%20actions)](https://github.com/features/actions)
[![Yandex.Cloud](https://img.shields.io/badge/-Yandex.Cloud-464646?style=flat-square&logo=Yandex.Cloud)](https://cloud.yandex.ru/)
# Продуктовый помощник
Приложение "Продуктовый помощник": сайт, на котором вы можете публиковать рецепты, добавлять чужие рецепты в избранное и подписываться на публикации других авторов. Сервис "Список покупок" позволяет пользователям создавать список продуктов, необходимых для приготовления выбранных блюд.

# Запуск проекта
## Запуск проекта в dev-режиме без Docker
### Клонируйте репозиторий на свой компьютер
#### HTTPS
```
git clone https://github.com/AleksSpace/foodgram-project-react.git
```
#### SSH
```
git clone git@github.com:AleksSpace/foodgram-project-react.git
```
#### GitHub CLI
```
git clone gh repo clone AleksSpace/foodgram-project-react
```
### Создайте и активируйте виртуальное окружение
```
python -m venv venv
```
```
. venv/Scripts/activate
```
### Обновите pip
```
python -m pip install --upgrade pip
```
### Перейдите (команда cd ...) в папку с файлом requirements.txt и установите зависимостси
```
pip install -r requirements.txt
```
## Создайте файл .env
С помощью команды cd перейдите в папку infra и введите команду для создания .env-файла
```
echo 'SECRET_KEY=some-secret-key
ALLOWED_HOSTS=*
DEBUG=1
DB_ENGINE=django.db.backends.postgresql # укажите, с какой БД вы работаете
DB_NAME=postgres # имя базы данных
POSTGRES_USER=<...> # логин для подключения к базе данных
POSTGRES_PASSWORD=<...> # пароль для подключения к базе данных (создайте свой собственный)
DB_HOST=<...> # название хоста (контейнера)
DB_PORT=<...> # порт для подключения к базе данных
' > .env
```
## Запуск проекта

#### Перейдите в папку backend и выполните команды
```
python manage.py migrate - Выполнение миграций
```
```
python manage.py createsuperuser - Создание суперпользователя
```
```
python manage.py loaddata fixtures/ingredients.json - Загрузка тестовой БД
```
```
python manage.py runserver localhost:8080 - Запуск Dev-сервера
```
## Проект будет доступен по ссылке:
http://localhost/

http://localhost/admin/
***
## Запуск проекта в контейнерах Docker
### Клонируйте репозиторий на свой компьютер
#### HTTPS
```
git clone https://github.com/AleksSpace/foodgram-project-react.git
```
#### SSH
```
git clone git@github.com:AleksSpace/foodgram-project-react.git
```
#### GitHub CLI
```
git clone gh repo clone AleksSpace/foodgram-project-react
```
### Создайте и активируйте виртуальное окружение
```
python -m venv venv
. venv/Scripts/activate
```
### Обновите pip и установите зависимостси
```
python -m venv venv
```
```
. venv/Scripts/activate
```
### Обновите pip
```
python -m pip install --upgrade pip
```
### Перейдите (команда cd ...) в папку с файлом requirements.txt и установите зависимостси
```
pip install -r requirements.txt
```
## Создайте файл .env
На production обязательно заменить значение SECRET_KEY
С помощью команды cd перейдите в папку infra и введите команду для создания .env-файла
```
echo 'SECRET_KEY=some-secret-key
ALLOWED_HOSTS=*
DEBUG=1
DB_ENGINE=django.db.backends.postgresql # укажите, с какой базой данных вы работаете
DB_NAME=postgres # имя базы данных
POSTGRES_USER=<...> # логин для подключения к базе данных
POSTGRES_PASSWORD=<...> # пароль для подключения к базе данных (создайте свой собственный)
DB_HOST=<...> # название хоста (контейнера)
DB_PORT=<...> # порт для подключения к базе данных
' > .env
```
## Сборка и запуск контейнеров локально на своем ПК.
Для этого вам понадобится установить приложение [Docker](https://www.docker.com/products/docker-desktop/) на свой ПК.
#### Для локального запуска необходимо отредактировать файл docker-compose.yml
Перейдите в папку infra и отредактируйте файл, в разделе web:
```
web:
    build:
      context: ../backend
      dockerfile: Dockerfile
    restart: always
    volumes:
      - static_backend_value:/code/static_backend/
      - media_data:/code/media/
    depends_on:
      - db
    env_file:
      - ./.env
```
в разделе frontend:
```
frontend:
    build:
      context: ../frontend
      dockerfile: Dockerfile
    volumes:
      - ../frontend/:/app/result_build/
    depends_on:
      - web
```
#### Для запуска из DockerHub необходимо в файле docker-compose.yml указать имя пользователя и название репозитория
Перейдите в папку infra и отредактируйте файл, в разделе web:
```
web:
    image: <Имя пользователя>/<Название репозитория>
    restart: always
    volumes:
      - static_backend_value:/code/static_backend/
      - media_data:/code/media/
    depends_on:
      - db
    env_file:
      - ./.env
```
в разделе frontend:
```
frontend:
    image: <Имя пользователя>/<Название репозитория>
    volumes:
      - ../frontend/:/app/result_build/
    depends_on:
      - web
```
### Сборка контейенеров
Перейдите в папку infra и запустите команду в терминале

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
docker compose exec web python manage.py loaddata fixtures/ingredients.json
```
***
## Проект будет доступен по ссылке:

API - http://localhost/

Redoc - http://localhost/api/docs/

Админка - http://localhost/admin/


## Deploy на сервер
При пуше в ветку master выполняется автоматическое разворачивание проекта на сервере (после всех тестов)
***
### Об авторе
- [Заикин Алексей](https://github.com/AleksSpace "GitHub аккаунт")
