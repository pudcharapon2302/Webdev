from urllib import request

from django.http import HttpResponse, HttpRequest
from django.urls import path
from blog.views import home

urlpatterns = [
    path('',home)
]