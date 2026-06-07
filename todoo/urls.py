from django.urls import path

from todoo import views


urlpatterns = [
    # Add Task
    path('', views.addtask, name= 'addtask'),
    # Mark as done
    path('mark_as_done/<int:pk>/', views.mark_as_done, name='mark_as_done'),
    # Mark as not done
    path('mark_as_not_done/<int:pk>/', views.mark_as_not_done, name='mark_as_not_done'),
    # edti task
    path('edit_task/<int:pk>/', views.edit_task, name='edit_task'),
    # delete task
    path('delete_task/<int:pk>/', views.delete_task, name='delete_task'),
]