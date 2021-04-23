Репозитарий

# https://github.com/alecs-shved/shops

Тестовое задание. Реализовать сервис, который принимает и отвечает на HTTP запросы..


Подготовка выполняем:

```
$ pip install pipenv

$ mkdir django-firecode

$ cd django-firecode

$ git init

$ git clone https://github.com/alecs-shved/shops

$ pipenv --python 3.6

$ pipenv shell

$ pipenv install django==2.1.7

$ django-admin startproject puppies

$ cd puppy_store

$ python manage.py startapp puppies

$ pipenv install djangorestframework==3.9.2

```

insert in settings.py
REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [],
    'TEST_REQUEST_DEFAULT_FORMAT': 'json'
}

### Database

Install **Postregs 12** and make a new database `fire-shops`.

```
$ sudo -i -u postgres
$ psql
$ CREATE NEW DATABASE fire-shops WITH OWNER=alecsander



```
change in settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'shops',
        'USER': 'alecsander',
        'PASSWORD': '2',
        'HOST': '127.0.0.1',
        'PORT': '5432'
    }
}
## Environment

Make sure you have Python 3.7:

```
$ python3 --version
Python 3.7.3
```
```
$ pipenv install psycopg2==2.7.7


$ python3 manage.py runserver
```



Проверяем работу экшонов по тестовому заданию

a. GET /city/ — получение всех городов из базы;
$ curl  -v -X POST --data '{"name": "Kupustin-Yar"}' -H "Content-Type: application/json"  http://127.0.0.1:8000/city/

$ curl  -v -X GET -H "Content-Type: application/json"  http://127.0.0.1:8000/city/

b. GET /city/street/ — получение всех улиц города;(city_id —
идентификатор города)
$ curl  -v -X POST --data '{"name":"Malina-street","city":1}' -H "Content-Type: application/json"  http://127.0.0.1:8000/city/street/

$ curl  -v -X GET -H "Content-Type: application/json"  http://127.0.0.1:8000/city/street/

c. POST /shop/ — создание магазина; Данный метод получает json c
объектом магазина, в ответ возвращает id созданной записи.
$ curl  -v -X POST --data '{"name":"shop-six","city":1, "street":1, "home":14, "time_open":"08:00", "time_close":"20:00"}' -H "Content-Type: application/json"  http://127.0.0.1:8000/shop/

d. GET /shop/?street=&city=&open=0/1 — получение списка магазинов;
i.
Метод принимает параметры для фильтрации. Параметры не
обязательны. В случае отсутствия параметров выводятся все
магазины, если хоть один параметр есть , то по нему
выполняется фильтрация.
ii.
Важно!: в объекте каждого магазина выводится название
города и улицы, а не id записей.
iii. Параметр open: 0 - закрыт, 1 - открыт. Данный статус
определяется исходя из параметров «Время открытия»,
«Время закрытия» и текущего времени сервера.
$ curl  -v -X GET -H "Content-Type: application/json"  http://127.0.0.1:8000/shop/?q=shop-six



end test ok!!