from django.shortcuts import render, redirect
from .forms import TaskForm
from .models import Task


def home(request):
    tasks = Task.objects.all()

    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {
        'tasks': tasks,
        'form': form,
    }
    return render(request, 'Tasks/home.html', context)


def update(request, pk):
    task = Task.objects.get(id=pk)

    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {
        'form': form,
    }
    return render(request, 'Tasks/update.html', context)


def delete(request, pk):
    task = Task.objects.get(id=pk)

    task.delete()

    return redirect('/')


def invert(request, pk):
    task = Task.objects.get(id=pk)

    task.is_completed = not(task.is_completed)
    task.save()

    return redirect('/')
