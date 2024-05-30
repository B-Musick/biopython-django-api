from django.contrib import admin
from django.urls import path
from file_upload_api.views import upload

urlpatterns = [
    # When hit path want to hit the view, import the view
    # Then need to connect this urls.py to the app
    path('upload', upload, name="upload"),
]
