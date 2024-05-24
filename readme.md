# Shell script
https://www.datacamp.com/tutorial/how-to-write-bash-script-tutorial
- Program that is interface to the operating system
- Shell derived since outermost layer around operating system
- Bash is a Unix command line interface responsible for interacting with a computer's operating system. Similarly to how movie scripts inform actors of what actions to take, a bash script tells the bash shell what to do. Thus, a bash script is a useful way to group commands to create a program. 

## Specify interpreter
```
#!/bin/bash
```
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
- Ensure the app you create is installed
- Install rest_framework [rest](https://www.django-rest-framework.org/)
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

# Entrez
https://www.youtube.com/watch?v=tl4xqdfIBh0&list=PLubh2aIGoECIGHR02Zy0cNNZwpVkxG00a&index=5&ab_channel=LanaDominkovic

https://github.com/lanadominkovic/12-days-of-biopython/blob/main/12_days_of_biopython/day_02/day_02-accessing-ncbi-databases.ipynb

# Got CORS errors when connecting to react, answer
https://stackoverflow.com/questions/44037474/cors-error-while-consuming-calling-rest-api-with-react

# Testing
- need to name function with 'test_' before so django finds it
https://www.django-rest-framework.org/api-guide/testing/

https://stackoverflow.com/questions/67082368/django-unit-test-not-working-reverse-for-xxx-is-not-found-xxx-is-not-a-valid

- Used this video for basic setup
https://www.youtube.com/watch?v=17KdirMbmHY&t=612s

- Django 
https://docs.djangoproject.com/en/5.0/topics/testing/