from django.contrib import admin
from django.urls import path

from klingon import views

app_name = "klingon"

urlpatterns = [
    path('', views.klingon_transcriber , name='klingon')
]
