from django.urls import path
from myapp.views import home, info, data, pdf

urlpatterns = [
    path('',home),
    path('info',info),
    path('data',data),
    path('pdf',pdf)
]