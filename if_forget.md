создаем новый джанго-проект

```shell
python -m django startproject <name_project> 
```

запуск django
```shell
python manage.py runserver
```

Проверить версию
```shell
python -m django --version
```
После чего создаем базовые миграции при первом запуске в корне проекта <name_project>
```shell
python manage.py migration
```

Дальше создаем супер пользователя
```shell
`python manage.py createsuperuser`
```

Теперь можно зайти в админку от суперпользователя с паролем, который был создан в БД

Вызвать помошника:
```shell
python manage.py help
```

Теперь можно создать новое приложение:
```shell
python manage.py startapp <name_app>
```
переходим в папку <name_project>.settings.py и вставить путь в INSTALLED_APPS

После создания новой модели обновляем миграцию при помощи
```shell
python manage.py makemigrations
```

Посмотреть обновление миграции можно так:
```shell
python manage.py showmigrations
```

Применяем новую миграцию для всех приложений:
```shell
python manage.py migrate
```

Применяем новую миграцию для конкретного приложения:
```shell
python manage.py migrate <app_name>
```

Что бы откатить миграцию используем:
```shell
python manage.py migrate <app_name> <нужную_версию_миграции>
```
Что бы НАкатить миграцию используем:
```shell
python manage.py migrate <app_name> <нужную_версию_миграции>
```