from django.urls import path
from .views import subject_list, topic_list

urlpatterns = [
    path('', subject_list, name='subjects'),
    path('subject/<int:subject_id>/', topic_list, name='topics'),
]