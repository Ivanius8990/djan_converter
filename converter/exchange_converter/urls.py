
from django.contrib import admin
from django.urls import path, include

from exchange_converter.views import index

urlpatterns = [
    path('', index, name='-'),
]
