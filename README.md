CRUD Operation-RestFramework Django with MYSQL

steps :
mkdir Rest-Django-Mysql
cd Rest-Django-Mysql
python3 -m venv env
source env/bin/activate
pip install django
pip install djangorestframework
django-admin startproject myproject
cd myproject
python3 manage.py startapp myapp

We also need to setup MySQL Database engine.
So open settings.py and change declaration of DATABASES:
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mytable',
        'USER': 'root',
        'PASSWORD': 'Amma4994@g',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}
```
