from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from users.views import register_view

urlpatterns = [
    path('register/', register_view,name="register"),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout')
]