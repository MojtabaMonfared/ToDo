from django.urls import path

from . import views

urlpatterns = [
    path('', views.ShowMode, name='showmode'),
    path('editmode/', views.CreateTask, name='editmode'),
    path('delete/<int:id>', views.DeleteTask, name='delete-task'),
    path('view/<int:pk>', views.TaskView, name='view-task'),
    
    path('tasks/', views.TasksList, name='tasks-list'),
    path('task/<int:pk>/edit', views.TaskEditForm, name='task-edit-form'),
]
