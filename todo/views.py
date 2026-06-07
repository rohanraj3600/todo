from asyncio import constants
from django.shortcuts import render
from todoo.models import  task

def home(request):
    # This is the home page of our app where we will show all the tasks and also add new tasks
    tasks = task.objects.filter(is_completed=False).order_by('-created_at')
    completed_task = task.objects.filter(is_completed=True).order_by('-created_at')
    constants = {'task1': tasks, 'completed_tasks': completed_task}
    return render(request, 'todo/home.html', constants)