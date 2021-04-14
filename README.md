CRUD Operation-RestFramework Django with MYSQL

steps :
```
mkdir Rest-Django-Mysql
cd Rest-Django-Mysql
python3 -m venv env
source env/bin/activate
pip install django
pip install djangorestframework
django-admin startproject myproject
cd myproject
python3 manage.py startapp myapp
```

We also need to setup MySQL Database engine.
So open settings.py and change declaration of DATABASES:
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mytable',
        'USER': 'root',
        'PASSWORD': '12345',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}
```
Now we open settings.py and add Django REST framework to the INSTALLED_APPS array here.
```
INSTALLED_APPS = [
    ...
    # Django REST framework 
    'rest_framework',
]
```
Install all application dependencies:
```
$ pip install -r requirements.txt
```
CORS Headers: Since we are building a standalone API server, we need to create a white list of approved web domains that are allowed to retrieve data from our API. This is known as Cross-Origin Resource Sharing (CORS).
granting all domains access to your API is a security issue in production, so it should only be done in a development environment. In production, you would specify the exact domains you want to grant access such as “www.aaaa.com”.
```
ALLOWED_HOSTS = [‘*’]
```
you should all of the migrations that will be executed:
```
pip install mysql-python
apt-get install python3-mysqldb libmysqlclient-dev python-dev
python manage.py migrate

Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying sessions.0001_initial... OK


python3 manage.py showmigrations

admin
 [X] 0001_initial
 [X] 0002_logentry_remove_auto_add
 [X] 0003_logentry_add_action_flag_choices
auth
 [X] 0001_initial
 [X] 0002_alter_permission_name_max_length
 [X] 0003_alter_user_email_max_length
 [X] 0004_alter_user_username_opts
 [X] 0005_alter_user_last_login_null
 [X] 0006_require_contenttypes_0002
 [X] 0007_alter_validators_add_error_messages
 [X] 0008_alter_user_username_max_length
 [X] 0009_alter_user_last_name_max_length
 [X] 0010_alter_group_name_max_length
 [X] 0011_update_proxy_permissions
contenttypes
 [X] 0001_initial
 [X] 0002_remove_content_type_name
sessions
 [X] 0001_initial
```
Now open myapp/apps.py, you can see TutorialsConfig class (subclass of django.apps.AppConfig).
This represents the Django app that we’ve just created with its configuration:
```
from django.apps import AppConfig


class MyappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myapp'
 ```
 Don’t forget to add this app to INSTALLED_APPS array in settings.py:
```
INSTALLED_APPS = [
    ...
   'myapp.apps.MyappConfig',
]
```
Configure CORS
We need to allow requests to our Django application from other origins.
In this example, we’re gonna configure CORS to accept requests from localhost:8081.

First, install the django-cors-headers library:

pip install django-cors-headers

In settings.py, add configuration for CORS:
```
INSTALLED_APPS = [
    ...
    # CORS
    'corsheaders',
]
```
You also need to add a middleware class to listen in on responses:
```
MIDDLEWARE = [
    ...
    # CORS
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
]
```

```
python3 manage.py runserver
```

Note: CorsMiddleware should be placed as high as possible, especially before any middleware that can generate responses such as CommonMiddleware.

Next, set CORS_ORIGIN_ALLOW_ALL and add the host to CORS_ORIGIN_WHITELIST:
```
CORS_ORIGIN_ALLOW_ALL = False
CORS_ORIGIN_WHITELIST = (
    'http://localhost:8081',
)
CORS_ORIGIN_ALLOW_ALL: If True, all origins will be accepted (not use the whitelist below). Defaults to False.
CORS_ORIGIN_WHITELIST: List of origins that are authorized to make cross-site HTTP requests. Defaults to [].

```
