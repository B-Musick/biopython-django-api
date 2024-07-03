from django.contrib import admin
from django.urls import path
from protein_api.views import uniprot
from . import views

urlpatterns = [
    # When hit path want to hit the view, import the view
    # Then need to connect this urls.py to the app
    path('uniprot', uniprot, name="uniprot"),
    path("", views.SwissProtRecordListCreate.as_view(), name="protein"),
    path("delete/<int:pk>/", views.SwissProtRecordDelete.as_view(), name="delete-protein"),
]
