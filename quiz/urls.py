from django.urls import path
from . import views

urlpatterns = [
    # Map URL /question ไปยัง view 'question'
    path('question', views.question, name='question'),

    # Map URL /question/create ไปยัง view 'create_question'
    path('question/create', views.create_question, name='create_question'),
]