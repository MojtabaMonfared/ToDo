from django.shortcuts import redirect, render
from django.views.generic import DeleteView

from .forms import TaskForm

from .models import Tasks
   
def EditMode(request):
    tasks = Tasks.objects.all()
    form = TaskForm()
    if request.method == 'POST':
        if request.POST.get('add_task'):
            form = TaskForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/editmode/')
        if request.POST.get('delete_task'):
            task = Tasks.objects.get(id=request.POST.get('task_id'))
            task.delete()
            return redirect('/editmode/')
            
    return render(request, 'todos/editmode.html', {'tasks': tasks, 'form': form, 'editmode': True})

def ShowMode(request):
    tasks = Tasks.objects.all()
    return render(request, 'todos/showmode.html', {'tasks': tasks})


def TaskEdit(request, id):
    task = Tasks.objects.get(id=id)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/editmode/%s' % id)
    return render(request, 'todos/task_edit.html', {'form': form})

def TaskView(request, id):
    task = Tasks.objects.get(id=id)
    return render(request, 'todos/task.html', {'task': task})