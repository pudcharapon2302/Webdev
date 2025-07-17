from django.urls import path
from quiz.views import quiz,create_question ,question

urlpatterns = [
    path('question',question),
    path('question/create',create_question),
]