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

