from django.urls import path
from . import views

urlpatterns = [
    path("sequences/", views.SequenceRecordListCreate.as_view(), name="sequence-list"),
    path("sequences/delete/<int:pk>", views.SequenceRecordDelete.as_view(), name="delete-sequence"),
]