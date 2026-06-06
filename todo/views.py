from asyncio import constants
from django.shortcuts import render
from todoo.models import  task

def home(request):
    tasks = task.objects.filter(is_completed=False).order_by('-created_at')
    constants = {'task1': tasks}
    return render(request, 'todo/home.html', constants)