from django.contrib import admin
from django.urls import path
from taskmanager.views import index,login,register,dashboard,create,invite,delete,logout,edit
import os
urlpatterns = [
    path('', index , name="index"),
    path('login', login , name="login"),
    path('register', register , name="register"),
    path('dashboard', dashboard , name="dashboard"),
    path('create-task', create , name="create"),
    path('invite/<id>', invite , name="invite"),
    path('delete/<id>', delete , name="delete"),
    path('edit/<id>', edit , name="edit"),
    path('logout', logout , name="logout"),
    
]
