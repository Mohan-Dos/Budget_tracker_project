from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('',loginpage,name='loginpage'),
    path('signup/',sigpage,name='signuppage')
]