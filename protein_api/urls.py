from django.contrib import admin
from django.urls import path
from protein_api.views import uniprot

urlpatterns = [
    # When hit path want to hit the view, import the view
    # Then need to connect this urls.py to the app
    path('uniprot', uniprot, name="uniprot"),
]
