from django.contrib import admin
from django.urls import path, include
from .views import home, work, about, user_login, register
import mainPage

urlpatterns = [
    path('', home, name='home'),
    path('work/', work, name='work'),
    path('about/', about, name='about_us'),
    path('login/', user_login, name='user_login'),
    path('register/', register, name='register'),
]

