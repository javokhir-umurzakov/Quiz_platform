from django.urls import path
from .views import start_quiz, quiz_question, check_answer, quiz_result

urlpatterns = [
    path('start/<int:topic_id>/', start_quiz, name='start_quiz'),
    path('question/', quiz_question, name='quiz_question'),
    path('check/', check_answer, name='check_answer'),
    path('result/', quiz_result, name='quiz_result'),

]