from django.urls import path

from . import views

urlpatterns = [
    path('', views.ShowMode, name='showmode'),
    path('editmode/', views.EditMode, name='editmode'),
    path('editmode/<int:id>', views.TaskEdit, name='task-edit'),
    path('task/<int:id>', views.TaskView, name='task-view'),
]
