from django.contrib import admin
from django.urls import path
from .views import GeneratePDF
urlpatterns = [
    path('', GeneratePDF.as_view()),
]
