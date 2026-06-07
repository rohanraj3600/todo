import http
from multiprocessing import context
from urllib import request

from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from .models import task

def addtask(request):
    tsk = request.POST['add_task']
    task.objects.create(title = tsk)
    return redirect('home')

def mark_as_done(request, pk):
    tsk = task.objects.get(id = pk)
    tsk.is_completed = True
    tsk.save()
    return redirect('home')

def mark_as_not_done(request, pk):
    tsk = task.objects.get(id = pk)
    tsk.is_completed = False
    tsk.save()
    return redirect('home')

def edit_task(request, pk):
    get_task = get_object_or_404(task, id=pk)
    if request.method == 'POST':
        new_task = request.POST['add_tasks']
        get_task.title = new_task
        get_task.save()
        return redirect('home')
    else:
        context={
            'get_task': get_task
        }
    return render(request, 'todo/edit.html' , context )

def delete_task(request, pk):
    get_task = get_object_or_404(task, id=pk)
    get_task.delete()
    return redirect('home')
