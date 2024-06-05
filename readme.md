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

# SeqFeatures
- Features are returned frm entrez efech
- They are returned are SeqFeature objects

## Attributes
type
    – This is a textual description of the type of feature (for instance, this will be something like ‘CDS’ or ‘gene’).
.location
    – The location of the SeqFeature on the sequence that you are dealing with, see Section 4.3.2 below. The SeqFeature delegates much of its functionality to the location object, and includes a number of shortcut attributes for properties of the location:

    .ref
        – shorthand for .location.ref – any (different) reference sequence the location is referring to. Usually just None.
    .ref_db
        – shorthand for .location.ref_db – specifies the database any identifier in .ref refers to. Usually just None.
    .strand
        – shorthand for .location.strand – the strand on the sequence that the feature is located on. For double stranded nucleotide sequence this may either be 1 for the top strand, −1 for the bottom strand, 0 if the strand is important but is unknown, or None if it doesn’t matter. This is None for proteins, or single stranded sequences. 

.qualifiers
    – This is a Python dictionary of additional information about the feature. The key is some kind of terse one-word description of what the information contained in the value is about, and the value is the actual information. For example, a common key for a qualifier might be “evidence” and the value might be “computational (non-experimental).” This is just a way to let the person who is looking at the feature know that it has not be experimentally (i. e. in a wet lab) confirmed. Note that other the value will be a list of strings (even when there is only one string). This is a reflection of the feature tables in GenBank/EMBL files.
.sub_features
    – This used to be used to represent features with complicated locations like ‘joins’ in GenBank/EMBL files. This has been deprecated with the introduction of the CompoundLocation object, and should now be ignored.

# SeqRecord
```
def convertSeqRecordsToString(records):
    string_records = []

       # records are in SeqRecord format, convert
    for rec in records:
        # print(rec.features[0]['DNA'])
        for feature in rec.features:
            print(feature.type)
        for annotation in rec.annotations:
            print(annotation+": ")
            print(rec.annotations[annotation])
        string_records.append({
            "id": rec.id,
            "seq": str(rec.seq),
            "name": rec.name,
            "description":rec.description,
            "dbxrefs": rec.dbxrefs,
            # "features": rec.features,
            # Will have to create a serializer for annotations
            "annotations": json.dumps(str(rec.annotations)),
            "letter_annotations": rec.letter_annotations
        })
    
    return string_records
```

# Work in virtual environment
```
python3 -m venv env
```

- Then to activate
```
source env/bin/activate
```
## Issues
- When creating got this error so had to install
```
The virtual environment was not created successfully because ensurepip is not
available.  On Debian/Ubuntu systems, you need to install the python3-venv
package using the following command.

    apt install python3.10-venv

You may need to use sudo with that command.  After installing the python3-venv
package, recreate your virtual environment.

Failing command: /home/brendan/Desktop/projects/biopython-django-api/biopython_api/env/bin/python3
```

# Requirements.txt
- Place all depenedencies here and install
https://www.freecodecamp.org/news/python-requirementstxt-explained/

```
pip install -r requirements.txt

```

# JWT Token
https://www.youtube.com/watch?v=vLTJ_03Dq4M
- JSON Web token
- Open standard defining self contained way for sequrly transmitting info between parties as JSON data
- Info is trusted since it is digitally signed using public private key pair (RSA)
- Use for authorization
    - Client signs in
    - Issued JWT token by backend
    - User will use this token to access the routes permitteb by token
    - Api validate the signature, calculated using heading and

## Parts
- Header
    - Type of token (eg. Bearer)
    - Type of algorithm (eg. RSA)
    - The contents of this header are base64URL encoded
- Payload
    - Have claims
        - Registerd (issuer, expiration, audience )
        - Public (Created to share info on those that agree)
        - Private
    ```
    {
        "username": "tim",
        "admin": true,
        "exp"
    }
    ```
- Signature

- All these are separated by periods

## Encrypting vs signing
- Encryption converts to form where cant be read, make sure to do this with sensitive data in token
- Signing - type of electronic signature that encypts documents with digital codes that are difficult to duplicate

## Signature
- Take encoded header, payload and secret key
- Then use RSA algorithm to sign the token
- This can be verified from the receiving party (user) - which will determine if valid without having secret key

## process
- User logs in, asks for token
    - Grant them Access token and refresh token
    - Front end stores both of these
- User uses the access token
- Validates
- Sends back JWT token to user with permissions
- Dont store in local storage
- Want to store in browser (httpOnly cookie) - accessible from browser but not JS
- JWT token needs to be sent to server through Authorization header

```
{
    "headers": {
        "Authorization": "Bearer HEADER.PAYLOAD.SIGNATURE"
    }
}
```

# ORM - object relational mapping
- Maps objects to code needing to be executed in the DB
- We can write python and django handles execution
- From api we accept JSON data and return it
- Need to create serializer to take python object and convert to JSON

# User
- Django has default user 
```
from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password", "email"]
        # Accept password when creating user, but dont return when giving data
        extra_kwargs = {"password": {"write_only": True}} 

        def create(self, validated_data):
            print(validated_data)
            # Method called when want to create new version of user
            # Serializer automatically looks at the fields and makes sure valid
            user = User.objects.create_user(**validated_data)
            return user

```

# Migrations
- When make changes to data model, need to run migrations
```
python manage.py makemigrations
```
- MAke the file saying the migrations that need
- Then to apply them run migration command, so proper tables setup

```
python manage.py migrate
```

# User auth
- Register user
- Submit user info to this route
```
/api/user/register
```

- Then need to request token with the following, and it will return access and refresh token
```
/api/token/
```

```
{
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcxNzY4NjM1NiwiaWF0IjoxNzE3NTk5OTU2LCJqdGkiOiIwNjU4N2IxNTEyODg0MzEzOTk3MzY2YzA4YWE0MWRmNCIsInVzZXJfaWQiOjN9.rzqWg_eOFLAqDisqetJcI7OCnilYvNKi_8aFShdn3Cc",
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE3NjAxNzU2LCJpYXQiOjE3MTc1OTk5NTYsImp0aSI6IjFjYzdlZGM2NDM5MDQxZTQ5ZThkNGY3MjYxZGZkNWZjIiwidXNlcl9pZCI6M30.l3xLvsCgQ3s8gesYx48aTx15GQeyf1cWnTMxsxp187I"
}
```

- Pass refresh token to get new access token
```
/api/token/refresh/
```