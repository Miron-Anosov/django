создаем новый джанго-проект

```shell
python -m django startproject <name_project> 
```

запуск django
```shell
python manage.py runserver
```


проверить версию
```shell
python -m django --version
```
после чего создаем базовые миграции при первом запуске в корне проекта <name_project>
```shell
python manage.py makemigrations
`python manage.py migration` 
```

дальше создаем супер пользователя
```shell
`python manage.py createsuperuser`
```

Теперь можно зайти в админку от суперпользователя с паролем, который был создан в БД

можно вызвать помошника
```shell
python manage.py help
```

Теперь можно создать новое приложение:
```shell
python manage.py startapp <name_app>
```
переходим в папку <name_project>.settings.py и вставить путь в INSTALLED_APPS