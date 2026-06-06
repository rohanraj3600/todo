from urllib import request

from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import task

def addtask(request):
    tsk = request.POST['add_task']
    task.objects.create(title = tsk)
    return redirect('home')