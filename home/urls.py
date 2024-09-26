from django.contrib import admin
from django.urls import path,include
from home.views import *

urlpatterns = [
    path('',loginpage,name='login'),
    path('home/', home,name='home'),
    path('about/',about,name='about'),
    path('team/',team,name='team'),
    path('register/',register,name='register'),
    path('contact/',contact,name='contact'),
    path('index/',index,name='index'),
    path('insert',insertData,name="insertData"),
    path('update/<id>',updateData,name="updateData"),
    path('delete/<id>',deleteData,name="deleteData"),
    
]
