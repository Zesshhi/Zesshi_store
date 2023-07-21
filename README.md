# Zesshi_store

===========

:heavy_check_mark: pip install -r requirements.txt

**To Do**

You need to rename ```github.env``` to ```.env``` and add info into that env file with your passwords and other settings

**To Change Develop / Production / Test settings**:

Change DJANGO_SETTINGS_MODULE in .env to:

```
'DJANGO_SETTINGS_MODULE'=ps_store.settings.dev_settings
```

```
DJANGO_SETTINGS_MODULE=unica_b2b.settings.prod_settings
```


**Docker**
-------------
1.Create docker container and images:

```
docker-compose -f docker-compose.yml up -d --build

OR

docker-compose -f docker-compose.prod.yml up -d --build
```

2.Create superuser

```
docker-compose -f docker-compose.prod.yml exec django python manage.py createsuperuser
```

3.Restart container

```
docker-compose down --remove-orphans

docker-compose down 
docker-compose -f <file_name.yml> up -d

OR

docker-compose down -v # to delete volumes

OR to restart models and static files

docker-compose -f <file_name.yml> restart
```

4.To see logs

```
docker-compose logs
```

Requirements:
-----------

To add external package do not use ```pip freeze```, for external packages we have pip-tools package which has
command ```pip-compile requirements.in``` before that you need to add name of your package in requirements.in file like
the others and then you can install your package with ```pip install -r requirements.txt```

To update requirements.txt use ```pip-compile --upgrade```