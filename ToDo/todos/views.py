from django.http import QueryDict
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages

from .forms import TaskForm

from .models import Tasks

created_message = "Task '%s' created successfully!"
deleted_message = "Task '%s' deleted successfully!"
edited_message = "Task '%s' edited successfully!"

# Show-mode where you can only watch tasks
def ShowMode(request):
    tasks = Tasks.objects.all()
    return render(request, 'todos/showmode.html', {'tasks': tasks})


# Create new task at editmode
def CreateTask(request):
    tasks = Tasks.objects.all()
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, created_message % form.cleaned_data['title'])
            return redirect('editmode')
    return render(request, 'todos/editmode.html', {'tasks': tasks, 'form': form, 'editmode': True})


# Delete a task by `id` in the url
def DeleteTask(request, id):
    task = Tasks.objects.get(id=id)
    task.delete()
    messages.add_message(request, messages.ERROR, deleted_message % task.title)
    return redirect('editmode')


# View all tasks
def TasksList(request):
    tasks = Tasks.objects.all()
    context = {'tasks': tasks}
    return render(request, 'todos/task.html', context)

# View tasks detail in new page
def TaskView(request, pk):
    task = get_object_or_404(Tasks, pk=pk)
    context = {'task': task}
    if request.method == 'GET':
        return render(request, 'todos/tasks.html', context)
    elif request.method == 'PUT':
        data = QueryDict(request.body).dict()
        form = TaskForm(data, instance=task)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, edited_message % task.title)
            return render(request, 'todos/partials/task-detail.html', context)
        context['form'] = form
        return render(request, 'todos/partials/task-details-form.html', context)

def TaskEditForm(request, pk):
    task = get_object_or_404(Tasks, pk=pk)
    form = TaskForm(instance=task)
    context = {
        'task': task,
        'form': form,
    }
    return render(request, 'todos/partials/task-details-form.html', context)
