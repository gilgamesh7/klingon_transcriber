from django.urls import path

from klingon import views

app_name = "klingon"

urlpatterns = [
    path('gettext/', views.klingon_transcriber , name='klingon'),
]
