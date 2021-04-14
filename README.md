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
