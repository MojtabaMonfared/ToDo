from django.shortcuts import redirect, render

from .forms import TaskForm

from .models import Tasks

def Home(request):
    tasks = Tasks.objects.all()
    form = TaskForm()
    if request.method == 'POST':
        if request.POST.get('add_task'):
            form = TaskForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/')
        if request.POST.get('delete_task'):
            task = Tasks.objects.get(id=request.POST.get('task_id'))
            task.delete()
            return redirect('/')
            
    return render(request, 'todos/index.html', {'tasks': tasks, 'form': form})