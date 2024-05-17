from django.contrib import admin
from django.urls import path
from entrez_api.views import search
from entrez_api.views import dbs_list

urlpatterns = [
    # When hit path want to hit the view, import the view
    # Then need to connect this urls.py to the app
    path('search', search),
    path('dbs_list', dbs_list),
]
