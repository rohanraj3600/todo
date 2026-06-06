from django.urls import path

from todoo import views

urlpatterns = [
    path('', views.addtask, name= 'addtask'),
]