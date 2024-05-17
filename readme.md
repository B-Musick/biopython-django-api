# Tutorial being used
https://docs.djangoproject.com/en/5.0/intro/tutorial01/

# Start project
```
django-admin startproject mysite
```

# Run Server
```
python3 manage.py runserver
```

# Database Setup
```
https://docs.djangoproject.com/en/5.0/intro/tutorial02/#database-setup
```

## Three step guide to changes to DB
We’ll cover them in more depth in a later part of the tutorial, but for now, remember the three-step guide to making model changes:

```
    Change your models (in models.py).
    Run python manage.py makemigrations to create migrations for those changes
    Run python manage.py migrate to apply those changes to the database.
```

## Activate models and migrate
```
https://docs.djangoproject.com/en/5.0/intro/tutorial02/#activating-models
```
```
python3 manage.py makemigrations biopython
```

### Run migrations and return the SQL
```
python3 manage.py sqlmigrate biopython 0001
```

# Project vs app
- Project is the root
- Can be many apps in project

## Create new app
```
python3 manage.py startapp sequence_api
```
## Playing wth DB API
https://docs.djangoproject.com/en/5.0/intro/tutorial02/#playing-with-the-api

# TODO:
## Create admin
https://docs.djangoproject.com/en/5.0/intro/tutorial02/#introducing-the-django-admin

# Model
- Translate how data will look from python code to sql code
- Django will translate the model to sql code
- Execute sql code and create that table
```
from django.db import models

# Create your models here.
class Gene(models.Model):
    sequence = models.CharField(max_length=200)
    published = models.DateTimeField()
    # translation = models.DateTimeField("date published")

    def __str__(self):
        return self.sequence


```

# Views
- Want to hit endpoint
- Class or function which will return data for specific endpoint
- View is responsible for creating the data and returning it

# Urls
- Create urls.py in new app

# Settings
```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'entrez_api',
    'rest_framework'
]
```