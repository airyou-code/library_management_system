from django.urls import path
from .views import register, user_login

urlpatterns = [
    path('register/', register, name='register'),
    path('', user_login, name='login'),
]
